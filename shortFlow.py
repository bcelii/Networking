
class ShortFlow:
	def __init__(self, bw_per_round):
		self.title = 'Long Flow'
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
			# print sizeQueues
			#longest distance
			difference = maxSize - minSize 
			#trying to find shortest distance to loop!
			for src in sizeDict.keys():
				if sizeDict[src] > minSize:
					# print sizeDict[src]
					if (sizeDict[src] - minSize) < difference:
						difference = sizeDict[src] - minSize
			if minSize == 0:
				for i in range(difference):
					for src in sizeDict.keys():
						if sizeDict[src] == difference:
							if bandwidth > 0:
								return_data.append(src.queue.popleft())
								bandwidth -= 50
								# print "pop"
			else:
				for i in range(minSize):
					for src in sizeDict.keys():
						if sizeDict[src] == minSize:
							if bandwidth > 0:
								return_data.append(src.queue.popleft())
								bandwidth -= 50
								# print "pop"
			# sizeQueues = []
			# for src in sources:
			# 	sizeQueues.append(len(src.queue))		
			# sizeQueues.sort()
			# print sizeQueues
			# print distance
			# bandwidth -= 50
		return return_data