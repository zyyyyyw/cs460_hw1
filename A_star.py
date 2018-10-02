from utils import *
import create_map
import math
import argparse

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
    return "path not found"


def init_H(graph, goal):
    h = {}
    for s in graph.getVertices():
        sx, sy = s.get_coord()
        gx, gy = goal
        h[s] = math.sqrt(2) * min([abs(sx - gx), abs(sy - gy)]) + max([abs(sx - gx), abs(sy - gy)]) - min(abs(sx - gx),
                                                                                                          abs(sy - gy))
    return h


def init_graph(graph, world_boundary, blacklist):
    x_list = [x for x, y in world_boundary]
    y_list = [y for x, y in world_boundary]
    x_min = min(x_list)
    y_min = min(y_list)
    x_max = max(x_list)
    y_max = max(y_list)
    for x in range(int(x_min), int(x_max+1), 1):
        for y in range(int(y_min), int(y_max+1), 1):
            graph.addVertex((x, y))
    list = graph.get_list()
    for node in list:
        node.setNeighbor(blacklist, graph)






def generatePath(node):
    list = []
    while not node == None:
        list.append(node.get_coord())
        node = node.parent
    return list[::-1]


if __name__ == "__main__":
    file_path = "map_1.txt"
    start = (1,1)
    goal = (2,2)
    world_bundary, obstacles, start_goal = create_map.load_map(file_path)
    blacklist = create_map.black_list(world_bundary, obstacles)
    graph = Graph()
    init_graph(graph, world_bundary, blacklist)
    print a_star(graph, start, goal)
