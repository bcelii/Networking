# FIFO

class FirstInFirstOut:
	def __init__(self, bw_per_round):
		self.title = 'FIFO'
		self.round_bw = bw_per_round

	def process_queues(self, sources):
		return_data = []
		bandwidth = self.round_bw
		#redistribute leftover bandwidth if there's an empty flow
		popsrc = sources[0]
		maxlength = 0
		maxTimeStamp = 0
		for src in sources:
			if len(src.queue) > maxlength:
				maxlength = len(src.queue)
				maxTimeStamp = src.queue[maxlength-1]['arrival_slot']
		while bandwidth > 0:
			minTimeStamp = maxTimeStamp
			for src in sources:
				if len(src.queue) > 0 and bandwidth >= 50:
					if (src.queue[0]['arrival_slot'] <= minTimeStamp):		
						popsrc = src
						minTimeStamp = src.queue[0]['arrival_slot']
			return_data.append(popsrc.queue.popleft())
			bandwidth -= 50
		return return_data



		