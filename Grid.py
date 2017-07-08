from Graph import Graph
from Node import Node
#import pdb

class Grid(Graph):
	def __init__(self, width, height):
		try:
			self.width = width
			self.height = height
			self.n = []
			for x in range(width):
				self.n.append([])
			for w in range(len(self.n)):
				for h in range(height):
					self.n[w].append(Node(str(w)+","+str(h)))
			for w in range(len(self.n)):
				for h in range(len(self.n[w])):
					b_l = w == 0
					b_r = w == width - 1
					b_t = h == 0
					b_b = h == height - 1
					if(not b_l and not b_t):
						self.n[w][h].add_neighbour(self.n[w-1][h-1], 1.4142)
					if(not b_r and not b_t):
						self.n[w][h].add_neighbour(self.n[w+1][h-1], 1.4142)
					if(not b_b and not b_r):
						self.n[w][h].add_neighbour(self.n[w+1][h+1], 1.4142)
					if(not b_l and not b_b):
						self.n[w][h].add_neighbour(self.n[w-1][h+1], 1.4142)
					if(not b_t):
						self.n[w][h].add_neighbour(self.n[w][h-1], 1)
					if(not b_b):
						self.n[w][h].add_neighbour(self.n[w][h+1], 1)
					if(not b_r):
						self.n[w][h].add_neighbour(self.n[w+1][h], 1)
					if(not b_l):
						self.n[w][h].add_neighbour(self.n[w-1][h], 1)

			flatten = lambda l: [item for sublist in l for item in sublist]
			self.nodes = flatten(self.n)
		except Exception as e:
			print(e)
		
		def find_node_position(self, node):
			for w in range(len(self.n)):
				for h in range(len(self.n[w])):
					if n[w][h]._name == node._name:
						return (w, h)
			else:
				raise "Node " + node._name + " not found in grid"

		def set_heuristic(self, target):
			for node in self.nodes:
				node.heuristic = self.manhattan(node, target)				

		def manhattan(self, node1, node2):
			s = find_node_position(node1)
			t = find_node_position(node2)
			return abs(s[0] - t[0]) + abs(s[1] - t[1]);
