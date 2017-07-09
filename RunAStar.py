from AStar import AStar;
from Grid import Grid;

try:
	print("---AStar---");
	grid = Grid(10, 10);
	grid.remove_node("0,3");
	grid.remove_node("0,4");
	grid.remove_node("2,1");
	grid.remove_node("2,3");
	grid.remove_node("2,4");
	grid.remove_node("2,6");
	grid.remove_node("2,9");
	grid.remove_node("3,3");
	grid.remove_node("3,6");
	grid.remove_node("3,7");
	grid.remove_node("4,3");
	grid.remove_node("4,6");
	grid.remove_node("5,2");
	grid.remove_node("5,3");
	grid.remove_node("6,4");
	grid.remove_node("6,5");
	grid.remove_node("6,8");
	grid.remove_node("7,0");
	grid.remove_node("7,2");
	grid.remove_node("7,4");
	grid.remove_node("7,6");
	grid.remove_node("7,7");
	grid.remove_node("9,0");
	grid.remove_node("9,1");
	astar = AStar(grid)

	initialNode = "0,0"
	targetNode = "9,9"
	print("Initial node: " + initialNode)
	print("Target node: " + targetNode)
	print("")
	nodes = astar.run(initialNode, targetNode)
	if nodes != None:
		print("Path:")
		for x in nodes:
			print(x._name)
	else:
		print("No path")
except Exception as e:
	print (e)

inp = input("\n===================\nPress ENTER to exit\n===================")