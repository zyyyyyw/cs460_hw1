import utils
import create_map
import math
def a_star(start, end):
    h = {}
    graph = init_graph()
    distance = {}
    visited = []
    queue = Queue.init()
   
    
    for node in graph.vertices
        distance[node] = None
    distance[start] = 0
    
    start.setParent(None)
    queue.enqueue(start, h[start])
    while (!queue.isEmpty):
        node = queue.dequeue()
        if(node.name == end) return node
        for neighbor in node.neigbors:
            if(neighbor not in visited):
                if(LineOfSight(node.parent,neighbor)):
                    if(distance[neighbor]!= None):
                        if((distance[node.parent]+graph.getDistance[node.parent, neighbor])<distance[neighbor]):
                            distance[neigbor] = distance[node.parent] + graph.getDistance[(node.parent, neighbor)]
                            neighbor.val = distance[neighbor]+h[neighbor]
                            neighbor.setParent(node.parent)
                    else:
                        distance[neighbor] = graph.getDistance[(node.parent, neighbor)]+distance[node.parent] /*calculate g()*/
                        queue.enqueue(neighbor, h[neighbor] + distance[neighbor])
                        neighbor.setParent(node.parent)
                else:
                    if(distance[neighbor]!= None):
                        if((distance[node]+graph.getDistance[node, neighbor])<distance[neighbor]):
                            distance[neigbor] = distance[node] + graph.getDistance[(node, neighbor)]
                            neighbor.val = distance[neighbor]+h[neighbor]
                            neighbor.setParent(node)
                    else:
                        distance[neighbor] = graph.getDistance[(node, neighbor)]+distance[node]
                        queue.enqueue(neighbor, h[neighbor] + distance[neighbor])
                        neighbor.setParent(node)
        visited.append(node)
    return None
def init_H(s, goal):
    sx,sy = start
    gx,gy = goal
    return sqrt(abs(sx-gx)**2+abs(sy-gy)**2)
def init_graph():

def LineOfSight(s, s’):
    x0 = s.x
    y0 = s.y
    x1 = s.x
    y1 = s.y
    f = 0
    dy := y1 − y0
    dx := x1 − x0
    if (dy < 0):
        dy = −dy
        sy = −1
    else
        sy = 1
    if (dx < 0):
        dx = −dx
        sx = −1
    else
        sx = 1
    if (dx >= dy):
        while (x0 != x1):
            f = f + dy
            if (f >= dx):
                if (x0 + ((sx − 1)/2), y0 + ((sy − 1)/2)) in blacklist:
                    return false
                y0 = y0 + sy
                f = f − dx
            if f (!= 0) || (x0 + ((sx − 1)/2), y0 + ((sy − 1)/2)) in blacklist:
                return false
            if dy = 0 || (x0 + ((sx − 1)/2), y0) in blacklist || (x0 + ((sx − 1)/2), y0 − 1) in blacklist:
                return false
            x0 = x0 + sx
    else
        while y0 != y1:
            f = f + dx
            if f >= dy:
                if (x0 + ((sx − 1)/2), y0 + ((sy − 1)/2)) in blacklist:
                    return false
                x0 = x0 + sx
                f = f − dy
            if f != 0 || (x0 + ((sx − 1)/2), y0 + ((sy − 1)/2)) in blacklist:
                return false
            if dx = 0 || (x0, y0 + ((sy − 1)/2)) in blacklist || (x0 − 1, y0 + ((sy − 1)/2)) in blacklist:
                return false
            y0 = y0 + sy
    return true