from packetsources import BurstySource, MediumConsistentSource, HoggingSource, SuperBursty
from roundrobin import RoundRobin
from fifo import FirstInFirstOut
from longFlow import LongFlow
from shortFlow import ShortFlow
from collections import deque

def main():
	#create different sources
	sources = [BurstySource(1), MediumConsistentSource(2), HoggingSource(3), SuperBursty(4)]
	
	sourceNames = ['BurstySource','MediumConsistentSource','HoggingSource','SuperBursty'];
	
	#get them to update themsevles
	for src in sources:
		src.add_to_queue();
		src.add_to_queue();
		src.add_to_queue();

	#print sources
	for x in range(len(sources)):
		print sourceNames[x]
		print "Length = " + str(len(sources[x].queue))
	
	#different tests for different bandwidths
	bandwidth = [0, 50, 100, 150, 200, 300, 400, 500, 600] #200, 400, 800];

	#test for Short Flow Algorithm
	'''f = open('noTraffic_Final','a')
	for band in bandwidth:
		for src in sources:
			src.reset()
			src.add_to_queue()
			src.add_to_queue()
			src.add_to_queue()

		print "For bandwidth = " + str(band);
		#initialize the algorithm
		SFlow = ShortFlow(band);

		#process the sources
		data = SFlow.process_queues(sources)
		#print "data = "
		#print data	

		#print the lengths of each flows now
		for x in range(len(sources)):
			print sourceNames[x];
			print "Length = " + str(len(sources[x].queue))'''

	#test for the Long flow algorithm:
	f = open('noTraffic_Final','a')
	for band in bandwidth:
		for src in sources:
			src.reset()
			src.add_to_queue()
			src.add_to_queue()
			src.add_to_queue()

		print "For bandwidth = " + str(band);
		#initialize the algorithm
		LFlow = LongFlow(band);

		#process the sources
		data = LFlow.process_queues(sources)
		#print "data = "
		#print data	

		#print the lengths of each flows now
		for x in range(len(sources)):
			print sourceNames[x];
			print "Length = " + str(len(sources[x].queue))



main();