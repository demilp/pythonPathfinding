from AStar import AStar;
from Grid import Grid;

try:
	print("---AStar---");
	grid = Grid(10, 10);
	grid.remove_node("3,0");
	grid.remove_node("1,1");
	grid.remove_node("2,1");
	grid.remove_node("3,1");
	grid.remove_node("2,2");
	grid.remove_node("0,3");
	grid.remove_node("2,3");
	grid.remove_node("1,5");
	grid.remove_node("2,5");
	grid.remove_node("3,5");
	grid.remove_node("1,6");
	grid.remove_node("6,6");
	grid.remove_node("7,6");
	astar = AStar(grid);

#	print("Connections:");
#	for node in enumerate(dijkstra.nodes):
#		for neighbour in enumerate(node[1].neighbours):
#			print(node[1]._name+", "+ neighbour[1][0]._name+", "+str(neighbour[1][1]));
#	print("");
	initialNode = "0,0";
	targetNode = "7,7";
	print("Initial node: " + initialNode);
	print("Target node: " + targetNode);
	print("");
	nodes = astar.run(initialNode, targetNode);
	if nodes != None:
		print("Path:");
		for x in nodes:
			print(x._name);
	else:
		print("No path");
except Exception as e:
	print (e);

inp = input("\n===================\nPress ENTER to exit\n===================");