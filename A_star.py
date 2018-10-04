from utils import *
import create_map
import math
import turtlebot_client

def a_star(graph, start, goal):
    h = init_H(graph, goal)
    distance = {}
    visited = []
    queue = Queue()
    start = graph.find_node(start)
    goal = graph.find_node(goal)
    for node in graph.getVertices():
        distance[node] = None
    distance[start] = 0
    start.setParent(None)
    queue.enqueue(start, h[start])
    i=0
    while not queue.isEmpty():
        node = queue.dequeue()
        if node == goal:
            return generatePath(node)
        for neighbor in node.get_neighbor():
            if neighbor not in visited:
                if distance[neighbor] is not None:
                    if (distance[node] + graph.getDistance(node, neighbor)) < distance[neighbor]:
                        distance[neighbor] = distance[node] + graph.getDistance(node, neighbor)
                        neighbor.val = distance[neighbor] + h[neighbor]
                        neighbor.setParent(node)
                else:
                    distance[neighbor] = graph.getDistance(node, neighbor) + distance[node]
                    queue.enqueue(neighbor, h[neighbor] + distance[neighbor])
                    neighbor.setParent(node)
        visited.append(node)
    return False


def init_H(graph, goal):
    h = {}
    for s in graph.getVertices():
        sx, sy = s.get_coord()
        gx, gy = goal
        h[s] = math.sqrt(2) * min([abs(sx - gx), abs(sy - gy)]) + max([abs(sx - gx), abs(sy - gy)]) - min(abs(sx - gx),
                                                                                                          abs(sy - gy))
    return h


def init_graph(graph, world_boundary, blacklist, intersect, obstacles, start, goal):
    x_list = [x for x, y in world_boundary]
    y_list = [y for x, y in world_boundary]
    x_min = min(x_list)
    y_min = min(y_list)
    x_max = max(x_list)
    y_max = max(y_list)
    for x in range(int(x_min), int(x_max + 1), 1):
        for y in range(int(y_min), int(y_max + 1), 1):
            graph.addVertex((x, y))
    list = graph.get_list()
    for node in list:
        node.setNeighbor(blacklist, intersect, obstacles, graph)
    x1, y1 = start
    if x1 % 1 != 0 or y1 % 1 != 0:
        graph.addVertex(start)
        start_v = graph.find_node(start)
        start_v.setNeighbor(blacklist, intersect, obstacles,graph)
    x2, y2 = goal
    if x2 % 1 != 0 or y2 % 1 != 0:
        graph.addVertex(goal)
        graph.find_node(goal).setNeighbor(blacklist, intersect, obstacles,graph, True)


def generatePath(node):
    list = []
    while not node == None:
        list.append(node.get_coord())
        node = node.parent
    return list[::-1]


if __name__ == "__main__":
    while True:
        file_path = input("Please enter the absolute path of the map file and press enter")
        try:
            map_file = open(file_path, 'r')
            info = map_file.read()
        except IOError:
            print "Error: File not found, please try again"
        except EOFError:
            print "Error: Empty File"
        else:
            map_file.close()
            break
    while True:
        start_input = input("Please enter the starting point in a x:y format. e.g. 3:4")
        x, y = start_input.split(':')
        try:
            x = float(x)
            y = float(y)
        except ValueError:
            print 'Error: Invalid input, please try again'
        else:
            start = (x,y)
            break
    while True:
        start_input = input("Please enter the goal point in a x:y format. e.g. 3:4")
        x, y = start_input.split(':')
        try:
            x = float(x)
            y = float(y)
        except ValueError:
            print 'Error: Invalid input, please try again'
        else:
            goal = (x,y)
            break
    world_bundary, obstacles, start_goal = create_map.load_map(info)
    blacklist, intersect, obstacles_list = create_map.black_list(world_bundary, obstacles)
    if start in blacklist or start in intersect or goal in blacklist or goal in intersect:
        print "No valid path is found"
        exit(0)
    graph = Graph()
    init_graph(graph, world_bundary, blacklist, intersect, obstacles_list, start, goal)
    path = a_star(graph, start, goal)
    if path:
        print "Valid path found"
        for coord in path:
            turtlebot_client.move_to_point(coord[0], coord[1], 0)
    else:
        print "No valid path is found"

