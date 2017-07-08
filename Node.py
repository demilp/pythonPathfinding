import sys
class Node:

	def __init__(self, name):
		self._name = name
		self.neighbours  = []
		self.parent = None
		self.cost = sys.maxsize
		self.heruistic = 0
		
	@property
	def fitness(self):
		return self.heruistic + self.cost

	def add_neighbour(self, neighbour, weight):
		self.neighbours.append((neighbour, weight))


