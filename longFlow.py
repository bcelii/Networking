#flow that will transmit will favor longer flows, procedure
#1) will give all bandwidth to flow with largest queue until it is tied 
#with a for the same legnth
#2) will keep distributing left over bandwidth between those that are same length
#until no bandwidth left over

class LongFlow:
	def __init__(self, bw_per_round):
		self.title = 'Long Flow'
		self.round_bw = bw_per_round

	def process_queues(self, sources):
		return_data = []
		bandwidth = self.round_bw
		#redistribute leftover bandwidth if there's an empty flow

		#get the id's of the queues with longest size
		while bandwidth > 0:
			maxSize = 0
			difference = 0
			sizeQueues = []
			sizeDict = {}
			for src in sources:
				sizeQueues.append(len(src.queue))
				sizeDict[len(src.queue)] = src
				
			sizeQueues.sort()
			maxSize = sizeQueues[len(sizeQueues)-1]
			difference = sizeQueues[len(sizeQueues)-1] - sizeQueues[len(sizeQueues)-2]
			# print sizeQueues
			# print difference

			# iterates the number of difference between the two longest packet source
			# if difference > 0:
			for i in range(difference):
				if bandwidth > 0:
					return_data.append(sizeDict[maxSize].queue.popleft())
					bandwidth -= 50
					# print "append"
			# else and then: Round Robin on the highest flow
			maxSize = 0
			difference = 0
			sizeQueues = []
			sizeDict = {}			
			for src in sources:
				sizeQueues.append(len(src.queue))
				sizeDict[src] = len(src.queue)	
			sizeQueues.sort()
			# print sizeQueues
			maxSize = sizeQueues[len(sizeQueues)-1]
			# print sizeDict
			for src in sizeDict.keys():
				if sizeDict[src] < maxSize:
					# return_data.queue.append(src.queue.popleft())
					# bandwidth -= 50
					if sizeDict[src] > difference:
						difference = sizeDict[src]
			for i in range(difference):		
				for src in sizeDict.keys():
					if sizeDict[src] == maxSize:
						if bandwidth > 0:
							return_data.append(src.queue.popleft())
							bandwidth -= 50
							# print "append"	
			# print sizeDict[maxSize]
			# sizeQueues = []
			# sizeDict = {}			
			# for src in sources:
			# 	sizeQueues.append(len(src.queue))
			# 	sizeDict[src] = len(src.queue)	
			# sizeQueues.sort()
			# print sizeQueues
		return return_data