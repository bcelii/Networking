#flow that will transmit will favor longer flows, procedure
#1) will give all bandwidth to flow with largest queue until it is tied 
#with a for the same legnth
#2) will keep distributing left over bandwidth between those that are same length
#until no bandwidth left over

class LongFlow:
	def __init__(self, bw_per_round):
		self.title = 'Long_Flow'
		self.round_bw = bw_per_round

	def process_queues(self, sources):
		return_data = []
		bandwidth = self.round_bw
		#redistribute leftover bandwidth if there's an empty flow

		#get the id's of the queues with longest size
		while bandwidth > 0:
			minSize = 0
			difference = 0
			sizeQueues = []
			sizeDict = {}
			for src in sources:
				sizeQueues.append(len(src.queue))
				sizeDict[src] = len(src.queue)				
			sizeQueues.sort()
			minSize = sizeQueues[0]
			maxSize = sizeQueues[len(sizeQueues)-1]

			difference = maxSize - minSize 
			#trying to find shortest distance to loop!
			for src in sizeDict.keys():
				if sizeDict[src] < maxSize:
					if (maxSize - sizeDict[src]) < difference:
						difference = maxSize - sizeDict[src]
			#print sizeQueues
			#print difference

			if difference != 0:
				for i in range(difference):
					for src in sizeDict.keys():
						if sizeDict[src] == maxSize:
							if bandwidth > 0:
								return_data.append(src.queue.popleft())
								bandwidth -= 50
								#print "pop"
			else:
				for i in range(minSize):
					for src in sizeDict.keys():
						if sizeDict[src] == minSize:
							if bandwidth > 0:
								return_data.append(src.queue.popleft())
								bandwidth -= 50
								#print "pop"
			if (sizeQueues[len(sizeQueues)-1] == 0 and bandwidth > 0):
				bandwidth = 0
			#for printing out sizes
			sizeQueues = []
			for src in sources:
				sizeQueues.append(len(src.queue))		
			sizeQueues.sort()
			#print sizeQueues
		return return_data