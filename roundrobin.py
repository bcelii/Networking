#round robin algorithm
from collections import deque

class RoundRobin:
	def __init__(self, bw_per_round):
		self.title = 'Round_Robin'
		self.round_bw = bw_per_round
		self.nextIndex = 0

	def process_queues(self, sources):
		#print sources
		#print sources[0].queue
		return_data = []
		bandwidth = self.round_bw
		totalServiced = 0;
		index = self.nextIndex
	#	print 'self.nextIndex = ' + str(self.nextIndex)
		lastServiceNotEmpty = 0
		#print bandwidth
		#redistribute leftover bandwidth if there's an empty flow
		while bandwidth >=50:
			totalServiced = 0;
			while index<len(sources):
				if len(sources[index].queue) > 0 and bandwidth >= 50:
					totalServiced +=1
					return_data.append(sources[index].queue.popleft())
					#print 'still in loop'
					bandwidth -= 50
					lastServiceNotEmpty = index
				index = index + 1
			if totalServiced == 0:
				bandwidth = 0
			else:
				index = 0
			

		#print 'about to return data'
		
		self.nextIndex = (lastServiceNotEmpty + 1)%4

		return return_data



		