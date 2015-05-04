class FirstInFirstOut:
	def __init__(self, bw_per_round):
		self.title = 'FIFO'
		self.round_bw = bw_per_round

	def process_queues(self, sources):
		return_data = []
		bandwidth = self.round_bw
		#redistribute leftover bandwidth if there's an empty flow
		popsrc = 0
		#maxlength = 0  --> don't think max length should be a factor
		#find maxTimeStamnp
		print "length of queue = " + str(len(sources[0].queue))
		for ii in range(len(sources)):
			if len(sources[ii].queue) != 0:
				popsrc = sources[ii]
				break

		if popsrc == 0:
			return return_data
		'''print (popsrc.queue)

		print "HELOOOO"
		print(popsrc)'''
		maxTimeStamp = popsrc.queue[len(popsrc.queue)-1]['arrival_slot'];

		for src in sources:
			if len(src.queue) > 0:
				if src.queue[len(src.queue)-1]['arrival_slot'] > maxTimeStamp:
					maxTimeStamp = src.queue[len(src.queue)-1]['arrival_slot']

		while bandwidth >= 50:

			#find minimum time stamp
			minTimeStamp = maxTimeStamp
			for src in sources:
				if len(src.queue) > 0:
					if src.queue[0]['arrival_slot'] < minTimeStamp:
						minTimeStamp = src.queue[0]['arrival_slot']
			#will have the minimum time stamp and go through and service all queues that
			#have a packet with this minimum time stamp in a round robin fashion
			sumQueues = 0
			for src in sources:
				#wil only service non-empty queues
				if len(src.queue) > 0:
					sumQueues += len(src.queue) #to check later if all the queues are empty
					if src.queue[0]['arrival_slot'] == minTimeStamp and bandwidth >= 50: #does the sneding if matches minTime and has alloted bandwidth
						return_data.append(src.queue.popleft())
						bandwidth -= 50

			#way to exit loop if all the sources are 0
			if(sumQueues <=0):
				bandwidth = 0
		print "returned some data"
		return return_data


		''''	if len(src.queue) > maxlength:
					maxlength = len(src.queue)
					maxTimeStamp = src.queue[maxlength-1]['arrival_slot']
			while bandwidth > 0:
				minTimeStamp = maxTimeStamp
				for src in sources:
					if len(src.queue) > 0 and bandwidth >= 50:
						if (src.queue[0]['arrival_slot'] <= minTimeStamp):		
							popsrc = src
							# minTimeStamp = src.queue[0]['arrival_slot']
				# print minTimeStamp
				if (len(popsrc.queue) > 0 and bandwidth > 0):
					return_data.append(popsrc.queue.popleft())
					bandwidth -= 50
				else:
					bandwidth -= 50

		return return_data'''