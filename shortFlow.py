
class ShortFlow:
	def __init__(self, bw_per_round):
		self.title = 'Short_Flow'
		self.round_bw = bw_per_round

	def process_queues(self, sources):
		#for src in sources:
		#	print src.title + "ID = " + str(src.source_id)
		return_data = []
		bandwidth = self.round_bw
		#redistribute leftover bandwidth if there's an empty flow
		minPacketSize = 50
		#get the id's of the queues with longest size
		#print "bandwidth before the loop = " + str(bandwidth)
		while bandwidth >= minPacketSize:
			#print "bandwidth after the loop = " + str(bandwidth)
			minSize = 0
			difference = 0
			sizeQueues = []
			sizeDict = {}
			for src in sources:
				sizeQueues.append(len(src.queue))
				sizeDict[src] = len(src.queue)				
			sizeQueues.sort() #sorts the list of lengths
			#print "sorted sizes = "
			#print sizeQueues
			minSize = sizeQueues[0]  #getn min and max size
			maxSize = sizeQueues[len(sizeQueues)-1]
			# print sizeQueues
			#longest distance
			difference = maxSize - minSize 
			#trying to find shortest distance to loop! --> gets distance from max to next closest
			for src in sizeDict.keys():
				if sizeDict[src] > minSize:
					# print sizeDict[src]
					if (sizeDict[src] - minSize) < difference:
						difference = sizeDict[src] - minSize
			if minSize == 0: #loop gets the next largest packet from 0 and
			#decrements that
				for i in range(difference):
					for src in sizeDict.keys():
						if sizeDict[src] == difference:
							if bandwidth >= minPacketSize:
								return_data.append(src.queue.popleft())
								bandwidth -= 50
								# print "pop"
			else: #will decrement the queue to 0 if there are non curently 0
				#print "inside no 0 queues"
				#print "minSize = " + str(minSize)
				#print ""
				for i in range(minSize):
					for src in sizeDict.keys():
						if sizeDict[src] == minSize:
							if bandwidth >= minPacketSize:
								return_data.append(src.queue.popleft())
								bandwidth -= 50
								# print "pop"

			sizeQueues = []
			for src in sources:
				sizeQueues.append(len(src.queue))		
			sizeQueues.sort()
			if sizeQueues[len(sizeQueues)-1] == 0 and bandwidth > 0:
				bandwidth = 0
			# print sizeQueues

			#"bandwidth before the loop = " + str(bandwidth)

		return return_data