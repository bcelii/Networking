from packetsources import BurstySource, MediumConsistentSource, HoggingSource, SuperBursty
from roundrobin import RoundRobin

NUM_ITERATIONS = 30

def main():
	#generate the sources
	sources = [BurstySource(1), MediumConsistentSource(2), HoggingSource(3), SuperBursty(4)]

	#create algorithm instance
	alg = RoundRobin(200)
	total_frame_delay = [0] * len(sources)
	total_frames_transmitted = [0] * len(sources)
	#loop for the number of iterations
	for i in range(NUM_ITERATIONS):
		#add necessary packets to queues
		for src in sources:
			src.add_to_queue()

		#process them queues, get back data
		data = alg.process_queues(sources)
		print 'round ' + str(i) + ': ' + str(data)
		for d in data:
			total_frame_delay[d['source_id']-1] += i - d['arrival_slot'] + 1
			total_frames_transmitted[d['source_id']-1] += 1

	#sum total slots waited for packets for each source
	for frame in total_frame_delay:
		print float(frame)/30
	for frame in total_frames_transmitted:
		print frame


main()

