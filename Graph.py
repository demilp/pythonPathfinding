from Node import Node

class Graph:

	nodes = []

	def remove_node(self, name):
		node = self.find_node(name)
		if node != None:
			self.nodes.remove(node)
		for x in self.nodes:
			for c in x.neighbours:
				if c[0] == node:
					x.neighbours.remove(c)

	def find_node(self, name):
		for node in self.nodes:
			if node._name == name:
				return node
		return None

				