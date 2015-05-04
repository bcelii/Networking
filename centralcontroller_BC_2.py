from packetsources import BurstySource, MediumConsistentSource, HoggingSource, SuperBursty
from roundrobin import RoundRobin
from fifo import FirstInFirstOut
from longFlow import LongFlow
from shortFlow import ShortFlow
from collections import deque
import os


NUM_ITERATIONS = 30

constantRun = {
	50:[9,1,31,27],
	100:[4/3,1,8.5,7],
	150: [1,1,1,1,875],
	200: [1,1,1,1.5],
	250: [1,1,1,1.375],
	300: [1,1,1,1.25],
	350: [1,1,1,1.125],
	400: [1,1,1,1],
	450: [1,1,1,1],
	500: [1,1,1,1],
}

def main():
	os.chdir("final_Data")
	#generate the sources
	#print 'Hello World'
	sources = [BurstySource(1), MediumConsistentSource(2), HoggingSource(3), SuperBursty(4)]
	sourceNames = ['BurstySource','MediumConsistentSource','HoggingSource','SuperBursty'];
	#loop that will generate the algorithms with different alotted bandwidth
	bandwidthValues = [50, 100, 150, 200,300, 400, 500, 750, 1000, 1500, 2000]
	f = open('noTraffic_Final','w')
	f.write('Flow, Bandwidth, Delay time\n')
	f.close()
	

	for src in sources:
		#will hold the delay and number of frames transmitted for different bandwidths
		total_frame_delay_band = {}
		total_frames_transmitted_band = {}
		for band in bandwidthValues:
			#generate the all the different algorithms
			RR = RoundRobin(band)
			#ensure timers and queues all reset
			src.reset()

			#cycle through the different number of sources and run the round 
			#on them to get baselines for delay time and throughput when no 
			#other traffic
			total_frame_delay = 0
			total_frames_transmitted = 0 

			for i in range(NUM_ITERATIONS):
				
				src.add_to_queue()
				#print "Bandwidth = "+ str(band) + " on iteration "+  str(i)
				#print src.queue
				#call for the round robin to service the individual source
				data = RR.process_queues([src])

				#update statistics passed ont the returned data
				for d in data:
					#print "data popped:"
					#print d
					#print 'd["arrival_slot"] =' + str(d['arrival_slot'])

					total_frame_delay += i -d['arrival_slot'] + 1
					total_frames_transmitted += 1
				#print "total_frame_delay = " + str(total_frame_delay)
				#print "total_frames_transmitted = " + str(total_frames_transmitted)
			counter = 0
			isempty = 0
			while isempty == 0:
				if src.queue != deque():
					#print "Bandwidth = "+ str(band) + " on iteration "+  str(counter) \
					#+ 'after normal'
					#print src.queue
					data = RR.process_queues([src])

					#update statistics passed ont the returned data
					for d in data:
						#print "data popped:"
						#print d
						#print 'd["arrival_slot"] =' + str(d['arrival_slot'])

						total_frame_delay += counter + NUM_ITERATIONS -d['arrival_slot'] + 1
						total_frames_transmitted += 1
					#print "total_frame_delay = " + str(total_frame_delay)
					#print "total_frames_transmitted = " + str(total_frames_transmitted)
					
				else:
					isempty = 1
				counter +=1
			#will clear out the rest of the buffer by so rest of delays get added

			total_frame_delay_band[band] = total_frame_delay
			total_frames_transmitted_band[band] = total_frames_transmitted
		#for band in bandwidthValues:
			#print 'total_frame_delay_band[' + str(band) + '] = ' + str(total_frame_delay_band[band])
			#print 'total_frames_transmitted_band[' + str(band) + '] = ' + str(total_frames_transmitted_band[band])
		

		#after go through all bandwidths then output to file
		f = open('noTraffic_Final','a')
		f.write(str(src.source_id)+',' + sourceNames[src.source_id-1] +',\n')		
		for band in bandwidthValues:
			frames =  total_frames_transmitted_band[band]
			delay =  total_frame_delay_band[band]
			#calculate the total delay
			f.write(','+str(band)+','+\
			str(float(delay)\
				/frames)+'\n')

		f.close()

			
main()	



