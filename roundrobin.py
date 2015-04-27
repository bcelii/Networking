#round robin algorithm

class RoundRobin:
	def __init__(self):
		self.title = 'Round Robin'
		self.round_bw = 100

	def process_queues(self, sources):
		return_data = []
		for src in sources:
			bandwidth = self.round_bw
			while bandwidth > 0 and len(src.queue) > 0:
				return_data.append(src.queue.popleft())
				bandwidth -= 50
		return return_data



		