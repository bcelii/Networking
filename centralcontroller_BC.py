from packetsources import BurstySource, MediumConsistentSource, HoggingSource, SuperBursty
from roundrobin import RoundRobin
from fifo import FirstInFirstOut
from longFlow import LongFlow
from shortFlow import ShortFlow

NUM_ITERATIONS = 30

def main():
	#generate the sources
	#print 'Hello World'
	sources = [BurstySource(1), MediumConsistentSource(2), HoggingSource(3), SuperBursty(4)]

	#loop that will generate the algorithms with different alotted bandwidth
	bandwidthValues = [50,100,150,200,250,300,350,400]
	f = open('noTraffic2','w')
	f.write('Flow, Bandwidth, Delay time')

	
	total_frame_delay_band = {}
	total_frames_transmitted_band = {};
	for band in bandwidthValues:
		#generate the all the different algorithms
		RR = RoundRobin(band);
		for counter in sources
			sources[counter].reset()
			

		#cycle through the different number of sources and run the round 
		#on them to get baselines for delay time and throughput when no 
		#other traffic
		for i in range(NUM_ITERATIONS):
			
			total_frame_delay = [0] * len(sources)
			total_frames_transmitted = [0] * len(sources)

			for src in sources:
				src.add_to_queue()

				#call for the round robin to service the individual source
				data = RR.process_queues([src]);

				#update statistics passed ont the returned data
				for d in data:
					#print d
					print 'd["arrival_slot"] =' + str(d['arrival_slot'])
					total_frame_delay[d['source_id']-1] += i -d['arrival_slot'] + 1
					total_frames_transmitted[d['source_id']-1] += 1
		total_frame_delay_band[band] = total_frame_delay
		total_frames_transmitted_band[band] = total_frames_transmitted

	for band in bandwidthValues:
		print total_frames_transmitted_band[band]


	#output the data to a file
	f = open('noTraffic','w')
	#f.write('Hellow there')
	f.write('Delay Output Single Flow No Traffic Round Robin')
	f.write('Flow, Bandwidth, Delay time')
	for src in sources:
		print total_frame_delay_band[50][0]
		print total_frames_transmitted_band[50][0]
		f.write(str(src.source_id)+','+',')
		for band in bandwidthValues:
			#calculate the total delay
			f.write(','+str(band)+','+\
			str(total_frame_delay_band[band][src.source_id-1]\
				/total_frames_transmitted_band[band][src.source_id-1]))

			
main()	
