from Node import Node
#import pdb
import time

class Dijkstra:

	def __init__(self, graph):
		self.graph = graph;

	def run(self, initialNode, targetNode):
		cost = 0;
		visited = [];
		initialNode = self.graph.find_node(initialNode);
		targetNode = self.graph.find_node(targetNode);
		if initialNode == None or targetNode == None:
			raise Exception("Could not find node with that name");
			return None;
		initialNode.cost = cost;
		queue = [];
		queue.append(initialNode);

		while len(queue) > 0:
			current = queue[0];
			if current == targetNode:
				break
			for neighbour in current.neighbours:
				if neighbour[1] not in visited and neighbour[0].cost > current.cost + neighbour[1]:
					neighbour[0].cost = current.cost + neighbour[1];
					neighbour[0].parent = current;
					if neighbour[0] not in queue:
						queue.append(neighbour[0]);
			visited.append(current);
			queue.remove(current);
			queue.sort(key=lambda n : n.cost);
		else:
			return None;
		current = queue[0];
		path = [current];
		while current.parent != None:
			path.append(current.parent);
			current = current.parent;
		path = path[::-1];
		return path;
			
