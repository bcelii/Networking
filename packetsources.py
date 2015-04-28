from collections import deque

class PacketSource:
	def __init__(self, id):
		self.queue = deque()
		self.source_id = id
		self.counter = 0

#adds three packets every other slot
class BurstySource(PacketSource):
	def __init__(self, id):
		PacketSource.__init__(self, id)

	def add_to_queue(self):
		if self.counter % 2 == 0:
			for i in range(3):
				new_dict = {}
				new_dict['arrival_slot'] = self.counter
				new_dict['source_id'] = self.source_id
				self.queue.append(new_dict)
		self.counter += 1

#adds a packet every other slot
class MediumConsistentSource(PacketSource):
	def __init__(self, id):
		PacketSource.__init__(self, id)

	def add_to_queue(self):
		if self.counter % 2 == 0:
			new_dict = {}
			new_dict['arrival_slot'] = self.counter
			new_dict['source_id'] = self.source_id
			self.queue.append(new_dict)
		self.counter += 1

class HoggingSource(PacketSource):
	def __init__(self, id):
		PacketSource.__init__(self, id)

	def add_to_queue(self):
		for i in range(3):
			new_dict = {}
			new_dict['arrival_slot'] = self.counter
			new_dict['source_id'] = self.source_id
			self.queue.append(new_dict)
		self.counter += 1

class SuperBursty(PacketSource):
	def __init__(self, id):
		PacketSource.__init__(self, id)

	def add_to_queue(self):
		if self.counter % 3 == 0:
			for i in range(8):
				new_dict = {}
				new_dict['arrival_slot'] = self.counter
				new_dict['source_id'] = self.source_id
				self.queue.append(new_dict)
		self.counter += 1







