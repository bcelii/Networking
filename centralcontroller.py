from packetsources import BurstySource, MediumConsistentSource, HoggingSource, SuperBursty
from roundrobin import RoundRobin
from fifo import FirstInFirstOut
from longFlow import LongFlow
from shortFlow import ShortFlow
from collections import deque

NUM_ITERATIONS = 2

def main():
	#generate the sources
	sources = [BurstySource(1), MediumConsistentSource(2), HoggingSource(3), SuperBursty(4), SuperBursty(5), SuperBursty(6)]

	#create algorithm instance
	alg = RoundRobin(300)
	total_frame_delay = [0] * len(sources)
	total_frames_transmitted = [0] * len(sources)
	#loop for the number of iterations
	for i in range(NUM_ITERATIONS):
		#add necessary packets to queues
		for src in sources:
			src.add_to_queue()

		#process them queues, get back data
		data = alg.process_queues(sources)

		print 'round ' + str(i) + str(data)
		for d in data:
			total_frame_delay[d['source_id']-1] += i - d['arrival_slot'] + 1
			total_frames_transmitted[d['source_id']-1] += 1

	counter = 0
	isempty = 0
	while isempty == 0:
		if src.queue != deque():
			#print "Bandwidth = "+ str(band) + " on iteration "+  str(counter) \
			#+ 'after normal'
			#print src.queue
			data = alg.process_queues(sources)

			#update statistics passed ont the returned data
			for d in data:
				#print "data popped:"
				#print d
				#print 'd["arrival_slot"] =' + str(d['arrival_slot'])

				total_frame_delay[d['source_id']-1] += counter + NUM_ITERATIONS -d['arrival_slot'] + 1
				total_frames_transmitted[d['source_id']-1] += 1
			#print "total_frame_delay = " + str(total_frame_delay)
			#print "total_frames_transmitted = " + str(total_frames_transmitted)
			
		else:
			isempty = 1
		counter +=1
	#will clear out the rest of the buffer by so rest of delays get added

	#sum total slots waited for packets for each source
	for frame in range (len(total_frame_delay)):
		print float(total_frame_delay[frame])/total_frames_transmitted[frame]
	'''for frame in total_frames_transmitted:
		print frame'''


	#Brendan Testing 4/28
	#testIndividualDelay(sources,algList)


main()



