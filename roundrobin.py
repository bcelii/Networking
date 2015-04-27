#round robin algorithm

class RoundRobin:
	def __init__(self, bw_per_round):
		self.title = 'Round Robin'
		self.round_bw = bw_per_round

	def process_queues(self, sources):
		return_data = []
		bandwidth = self.round_bw
		#redistribute leftover bandwidth if there's an empty flow
		while bandwidth > 0:
			for src in sources:
				if len(src.queue) > 0 and bandwidth >= 50:
					return_data.append(src.queue.popleft())
					bandwidth -= 50
		return return_data



		