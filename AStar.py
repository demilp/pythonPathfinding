from Node import Node
#import pdb
import time

class AStar:

	def __init__(self, graph):
		self.graph = graph

	def run(self, initialNode, targetNode):
		visited = []
		initialNode = self.graph.find_node(initialNode)
		targetNode = self.graph.find_node(targetNode)
		if initialNode == None or targetNode == None:
			raise Exception("Could not find node with that name")

		self.graph.set_heuristic(targetNode)
		initialNode.cost = 0
		queue = []
		queue.append(initialNode)

		while len(queue) > 0:
			current = queue[0]
			if current == targetNode:
				break
			for neighbour in current.neighbours:
				if neighbour[0] not in visited and neighbour[0].cost > current.cost + neighbour[1]:
					neighbour[0].cost = current.cost + neighbour[1]
					neighbour[0].parent = current
					if neighbour[0] not in queue:
						queue.append(neighbour[0])
			visited.append(current)
			queue.remove(current)
			queue.sort(key = lambda n : n.fitness)



		else:
			return None

		for n in visited:
			print(n._name)




		current = queue[0]
		path = [current]
		while current.parent != None:
			path.append(current.parent)
			current = current.parent
		path = path[::-1]
		return path
			
