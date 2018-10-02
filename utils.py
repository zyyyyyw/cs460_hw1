import math
class Graph:
    def __init__(self):
        self.vertices = []
        self.distances = {}

    def addVertex(self, xy):
        x,y = xy
        xy = (float(x),float(y))
        node = Node(xy)
        self.vertices.append(node)

    def addEdge(self, node1, node2):
        x1,y1 = node1.get_coord()
        x2,y2 = node2.get_coord()
        weight = math.sqrt(abs((x1 - x2) ** 2 + abs((y1 - y2) ** 2)))
        self.distances[(node1, node2)] = weight


    def getDistance(self, node1, node2):
        return self.distances[(node1, node2)]

    def getVertices(self):
        return self.vertices

    def find_node(self,xy):
        for node in self.vertices:
            if node.get_coord() == xy:
                return node

    def get_list(self):
        return self.vertices

    def get_weight(self):
        return self.distances



class Queue:
    def __init__(self):
        self.list = []

    def enqueue(self, node, val):
        node.setVal(val)
        self.list.append(node)
        self.list = sorted(self.list, key=lambda x: x.get_val())

    def dequeue(self):
        if not self.list==[]:
            head = self.list[0]
            self.list = self.list[1:]
            return head
        else:
            return None

    def isEmpty(self):
        if self.list is not []:
            return False
        else:
            return True
    # def isInQueue(node):


class Node:
    def __init__(self, coord):
        self.coord = coord
        self.nt = None
        self.val = None
        self.neighbors = []


    def setVal(self, val):
        self.val = val

    def setNeighbor(self, blacklist, graph):
        p_neighbor = self.potentialNeighbor()
        list = []
        for coord in p_neighbor:
            if coord not in blacklist:
                list.append(coord)
        if not list==[]:
            for xy in list:
                neighbor = graph.find_node(xy)
                if not neighbor == None:
                    self.neighbors.append(neighbor)
                    graph.addEdge(self, neighbor)

    def setParent(self, node):
        self.parent = node

    def get_coord(self):
        return self.coord

    def potentialNeighbor(self):
        x,y = self.coord
        return [(x - 1, y), (x - 1, y - 1), (x, y - 1), (x + 1, y + 1), (x + 1, y), (x, y + 1), (x + 1, y - 1),
                (x - 1, y + 1)]

    def get_neighbor(self):
        return self.neighbors

    def get_val(self):
        return self.val
