from utils import *
import create_map
import math
def a_star(graph, start, goal):

    h = init_H(graph, goal)
    distance = {}
    visited = []
    queue = Queue()
   
    
    for node in graph.getVertices:
        distance[node] = None
    distance[start] = 0
    start.setParent(None)
    queue.enqueue(start, h[start])
    while (!queue.isEmpty):
        node = queue.dequeue()
        if(node.name == goal): return generatePath(node)
        for neighbor in node.neigbors:
            if(neighbor not in visited):
                if(distance[neighbor]!= None)
                    if((distance[node]+graph.getDistance[node, neighbor])<distance[neighbor])
                        distance[neigbor] = distance[node] + graph.getDistance[(node, neighbor)]
                        neighbor.val = distance[neighbor]+h[neighbor]
                        neighbor.setParent(node)
                else:
                    distance[neighbor] = graph.getDistance[(node, neighbor)]+distance[node]
                    queue.enqueue(neighbor, h[neighbor] + distance[neighbor])
                    neighbor.setParent(node)
        visited.append(node)
    return "path not found"
def init_H(grahp, goal):
    h = {}
    for s in getVertices() 
        sx,sy = s
        gx,gy = goal
        h[s] = math.sqrt(2)*min([abs(sx-gx), abs(sy,gy)])+max([abs(sx-gx), abs(sy,gy)])-min(abs(sx-gx), abs(sy,gy))
    return h
    
def init_graph(grahp, world_boundary, blacklist):
    x_list = [x for x,y in world_boundary]
    y_list = [y for x,y in world_boundary]
    x_min = min(x_list)
    y_min = min(y_list)
    x_max = max(x_list)
    y_max = max(y_list)
    while(x_min<=x_max):
        while(y_min<=x_max):
            neighors = potentialNeighbor(x_min,y_min)
            for point in neigbors
                if(point not in blacklist):
                    x,y = point
                    graph.addVertex(point)
                    graph.addEdge((x_min,y_min),point, math.sqrt(abs((x - x_min)**2+abs((y - y_min)**2))))
            y_min += 1
        x_min += 1
            
def potentialNeighbor(x, y):
    return [(x-1, y), (x-1, y-1), (x, y-1), (x+1,y+1), (x+1,y),(x, y+1), (x+1,y-1), (x-1,y+1)]

def generatePath(node):
    
    

world_boundary, obstacles, start_goal = load_map('map_1.txt')
grahp = Graph()
init_graph(grahp, world_boundary, blacklist)