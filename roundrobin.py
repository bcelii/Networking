#round robin algorithm

class RoundRobin:
	def __init__(self, bw_per_round):
		self.title = 'Round_Robin'
		self.round_bw = bw_per_round

	def process_queues(self, sources):
		#print sources
		#print sources[0].queue
		return_data = []
		bandwidth = self.round_bw
		totalServiced = 0;
		#print bandwidth
		#redistribute leftover bandwidth if there's an empty flow
		while bandwidth >=50:
			totalServiced = 0;
			for src in sources:
				if len(src.queue) > 0 and bandwidth >= 50:
					totalServiced +=1
					return_data.append(src.queue.popleft())
					#print 'still in loop'
					bandwidth -= 50
			if totalServiced == 0:
				bandwidth = 0

		#print 'about to return data'
		return return_data



		