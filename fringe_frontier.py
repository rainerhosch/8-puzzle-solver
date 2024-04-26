
# This handler for stack fringe data structure, based LIFO algorithm
class StackFrontier:
	def __init__(self):
		self.frontier = []

	def add(self, node):
		self.frontier.append(node)

	def contains_state(self, state):
		return any((node.state[0] == state[0]).all() for node in self.frontier)
	
	def empty(self):
		return len(self.frontier) == 0
	
	def remove(self):
		if self.empty():
			raise Exception("Empty Frontier")
		else:
			node = self.frontier[-1]
			self.frontier = self.frontier[:-1]
			return node

# This handler for queue fringe data structure, based FIFO algorithm
class QueueFrontier(StackFrontier):
	def remove(self):
		if self.empty():
			raise Exception("Empty Frontier")
		else:
			node = self.frontier[0]
			self.frontier = self.frontier[1:]
			return node