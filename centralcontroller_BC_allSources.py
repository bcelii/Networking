from packetsources import BurstySource, MediumConsistentSource, HoggingSource, SuperBursty
from roundrobin import RoundRobin
from fifo import FirstInFirstOut
from longFlow import LongFlow
from shortFlow import ShortFlow
from collections import deque
import os


NUM_ITERATIONS = 2
sizeOfPackets = 50

highNumber = 5
diffNumber = 2

def numberSources(option):
	if option == 0:
		return 1
	else :
		return highNumber

def add_to_queue_AllSources(sources):
	for src in sources:
		src.add_to_queue()

def reset_AllSources(sources):
	for src in sources:
		src.reset()


def main():
	#change paths to the data folder
	os.chdir("New_Data")

	#create testing environment for different number of sources
	sourceNames = ['BurstySource','MediumConsistentSource','HoggingSource','SuperBursty'];
	sourceContructors = [BurstySource, MediumConsistentSource, HoggingSource, SuperBursty];
	#create different objects that define the different testing environment
	#Each source will either have high or low number of those types of sources
	#Ex: one environment might have
	#: 1 BurstySource (low)
	#: 5 MediumConsistentSource (high)
	#: 5 HoggingSource (high)
	#: 1 SuperBursty (low)
	

	testEnvironment = []

	counterNumber = 0;
	for a in range(diffNumber):
		for b in range(diffNumber):
			for c in range(diffNumber):
				for d in range(diffNumber):
					
					testEnvironment.append( [
						numberSources(a),
						numberSources(b),
						numberSources(c),
						numberSources(d),

					])
					counterNumber += 1

	'''for item in testEnvironment:
		print item
		print ""  '''
	#exit()

	#exit() #breakpoint to see only the different environments printed
	#have all testing environment --> iterat through all them
	for test in testEnvironment:
		#create the different sources
		
		#the id number will correspond to what type of source it is 
		sources = []
		sourceFunct = {}
		for i in range(len(test)):
			sourceFunct = sourceContructors[i]
			for jj in range(test[i]):

				sources.append(sourceFunct(i))
				

		#should have all packet sources

		'''for src in sources:
			print src.title + "ID = " + str(src.source_id)

		print " "
		print ""
		continue'''

		#iterate through different algorithms
		algorithmConstructors = [FirstInFirstOut, RoundRobin,LongFlow,ShortFlow]
		#algNames = ["FirstInFirstOut","RoundRobin","LongFlow","ShortFlow"]
		'''algorithm = [];
		for i in range(len(algorithmConstructors)):
			algorithm.append({
				algNames[i]:algorithmConstructors[i]
				})'''

		
		for alg in algorithmConstructors:
			
			filenameEnd = ("_"+ alg(0).title +
				" Bursty = " + str(test[0]) + 
				" Medium = " + str(test[1]) + 
				" Hogging = " + str(test[2]) + 
				" SupBurst = " + str(test[3]))

			open('delay'+filenameEnd, 'w').close()

			f = open('delay'+filenameEnd,'w')
			f.write('average_pcket_delay'+filenameEnd+'\n')
			f.write('\n');

			f.write('Bandwidth,'+(',').join(sourceNames))
			
			f.close()

			#do header for the throughput file:
			open('throughput'+filenameEnd, 'w').close()

			f = open('throughput'+filenameEnd,'w')
			f.write('average_throughput'+filenameEnd+'\n')
			f.write('\n');
			#f.write('HELOOOOOO')

			f.write('Bandwidth,'+(',').join(sourceNames))
			
			f.close()
			
			
			#total_frames_transmitted_band = []
			bandwidth = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]

			#iterate through all bandwidths

			for band in bandwidth:
				#do header for the packet delay file:
			

				#ensure timers and queues all reset
				reset_AllSources(sources)

				#create the algorithm
				algorithm = alg(band)

				#for the number of sources initialize the containers for stats
				sources_stats = []
				for i in range(len(sourceNames)) :
					sources_stats.append({
						'total_frame_delay' : 0,
						'total_frames' : 0,
						'total_throughput' : 0
					});


				#total_frame_delay = 0
				#total_frames_transmitted = 0 

				for i in range(NUM_ITERATIONS):
				
					add_to_queue_AllSources(sources)
					#print "Bandwidth = "+ str(band) + " on iteration "+  str(i)
					#print src.queue
					#call for the round robin to service the individual source
					data = algorithm.process_queues(sources)

					#update statistics passed ont the returned data
					for d in data:
						#print "data popped:"
						#print d
						#print 'd["arrival_slot"] =' + str(d['arrival_slot'])


						sources_stats[d['source_id']]['total_frame_delay'] += i -d['arrival_slot'] + 1
						sources_stats[d['source_id']]['total_frames']+= 1
						sources_stats[d['source_id']]['total_throughput']+= 1*sizeOfPackets
					#print "total_frame_delay = " + str(total_frame_delay)
					#print "total_frames_transmitted = " + str(total_frames_transmitted)
				
				counter = 0
				isempty = 0

				#will process those still waiting in the queue so that they add to overall delay
				while isempty == 0:

					#check to see if all of the queues are empty
					allQueuesEmpty = 0
					for src in sources:
						if src.queue != deque():
							allQueuesEmpty = 1
							break

					if allQueuesEmpty == 1:
							counter +=1
							#print "Bandwidth = "+ str(band) + " on iteration "+  str(counter) \
							#+ 'after normal'
							#print src.queue
							data = algorithm.process_queues(sources)

							#update statistics passed ont the returned data
							for d in data:
								#print "data popped:"
								#print d
								#print 'd["arrival_slot"] =' + str(d['arrival_slot'])

								sources_stats[d['source_id']]['total_frame_delay'] += counter + NUM_ITERATIONS -d['arrival_slot'] + 1
								sources_stats[d['source_id']]['total_frames'] += 1
								#***********throughput is excluded from this calculation because then would 
								#***********always send the same number of packets receivced******

								#sources_stats[d['source_id']].total_frames+= 1
							#print "total_frame_delay = " + str(total_frame_delay)
							#print "total_frames_transmitted = " + str(total_frames_transmitted)
					else:
						isempty = 1

				#end of processing for certian bandwidth
				f_delay = open('delay' + filenameEnd,'a')
				f_delay.write("\n")
				#combine results into string
				delay_statsString = ""
				for srcStats in sources_stats:
					delay_statsString += ","+str(srcStats['total_frame_delay']/srcStats['total_frames'])

				f_delay.write(str(band) + delay_statsString)
				f_delay.close()

				f_thr = open('throughput'+filenameEnd, 'a')
				f_thr.write("\n")
				thr_statsString = ""
				
				for jj in range(len(sources_stats)):
					thr_statsString += "," + str(sources_stats[jj]['total_throughput']/test[jj])
				'''	
				for srcStats in sources_stats:
					thr_statsString += ","+str(srcStats['total_throughput']/)'''

				f_thr.write(str(band) + thr_statsString)
				f_thr.close()



main()