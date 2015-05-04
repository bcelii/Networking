from packetsources import BurstySource, MediumConsistentSource, HoggingSource, SuperBursty
from roundrobin import RoundRobin
from fifo import FirstInFirstOut
from longFlow import LongFlow
from shortFlow import ShortFlow
from collections import deque
import os


NUM_ITERATIONS = 10
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

	source_flows = [BurstySource, MediumConsistentSource, HoggingSource, SuperBursty];
	algorithmConstructors = [LongFlow]
	for alg in algorithmConstructors:
		#create a new file
		#run the algorithms, getting back total frame delay
		bandwidth_values = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]
		avg_delay_val = []
		for test in testEnvironment:
			total_frame_delay = 0
			total_frames_transmitted = 0
			sources = []
			sourceFunct = {}
			for i in range(len(test)):
				sourceFunct = source_flows[i]
				for jj in range(test[i]):
					sources.append(sourceFunct(i))
				
			for band in bandwidth_values:

				for src in sources:
					src.reset()
				current_alg = alg(band)
				new_file = "avg_delay_file " + current_alg.title

				for i in range(NUM_ITERATIONS):
					#add necessary packets to queues
					for src in sources:
						src.add_to_queue()

					#process them queues, get back data
					data = current_alg.process_queues(sources)
					#print 'round ' + str(i) + ': ' + str(data)
					for d in data:
						total_frame_delay += i - d['arrival_slot'] + 1
						total_frames_transmitted += 1

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
							data = current_alg.process_queues(sources)

							#update statistics passed ont the returned data
							for d in data:
								#print "data popped:"
								#print d
								#print 'd["arrival_slot"] =' + str(d['arrival_slot'])

								total_frame_delay += counter + NUM_ITERATIONS -d['arrival_slot'] + 1
								total_frames_transmitted += 1
								#***********throughput is excluded from this calculation because then would 
								#***********always send the same number of packets receivced******

								#sources_stats[d['source_id']].total_frames+= 1
							#print "total_frame_delay = " + str(total_frame_delay)
							#print "total_frames_transmitted = " + str(total_frames_transmitted)
					else:
						isempty = 1

			avg_delay_val.append(float(total_frame_delay)/total_frames_transmitted)

		
		with open(new_file, 'w') as write_file:
			for i in range(len(avg_delay_val)):
				write_file.write(str(i) + ', ' + str(avg_delay_val[i]) + "\n")



main()

		#add data to file