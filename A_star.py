import Queue
import Graph
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
    return None
def init_H(points, vals):
def init_graph():