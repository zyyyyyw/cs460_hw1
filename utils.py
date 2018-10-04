import math


class Graph:
    def __init__(self):
        self.vertices = []
        self.distances = {}

    def addVertex(self, xy):
        x, y = xy
        xy = (float(x), float(y))
        node = Node(xy)
        self.vertices.append(node)

    def addEdge(self, node1, node2):
        x1, y1 = node1.get_coord()
        x2, y2 = node2.get_coord()
        weight = math.sqrt(abs((x1 - x2) ** 2 + abs((y1 - y2) ** 2)))
        self.distances[(node1, node2)] = weight

    def getDistance(self, node1, node2):
        return self.distances[(node1, node2)]

    def getVertices(self):
        return self.vertices

    def find_node(self, xy):
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
        head = self.list[0]
        self.list = self.list[1:]
        return head

    def isEmpty(self):
        if self.list:
            return False
        else:
            return True


class Node:
    def __init__(self, coord):
        self.coord = coord
        self.nt = None
        self.val = None
        self.neighbors = []

    def setVal(self, val):
        self.val = val

    def setNeighbor(self, blacklist, intersect, obstacles, graph, goal=False):
        p_neighbor = self.potentialNeighbor()
        neighbor_list = self.filter_neighbor(p_neighbor,blacklist,intersect,obstacles)
        if neighbor_list is not []:
            for xy in neighbor_list:
                neighbor = graph.find_node(xy)
                if not neighbor is None:
                    self.neighbors.append(neighbor)
                    graph.addEdge(self, neighbor)
        if goal and neighbor_list is not []:
            for neighbor_coord in neighbor_list:
                neighbor = graph.find_node(neighbor_coord)
                if neighbor is not None:
                    neighbor.add_neighbor(self)
                    graph.addEdge(neighbor, self)

    def filter_neighbor(self,neighbors,blacklist, intersect,obstacles):
        neighbor_list = []
        coord = self.coord
        for neighbor in neighbors:
            if neighbor not in blacklist:
                if neighbor[0] != coord[0] and neighbor[1] != coord[1]:
                    x1, y1 = coord
                    x2, y2 = neighbor
                    if (x1, y2) not in blacklist and (x2, y1) not in blacklist:
                        neighbor_list.append(neighbor)
                    else:
                        switch = True
                        for obstacle in obstacles:
                            if (x1, y2) in obstacle and  (x2, y1) in obstacle:
                                switch = False
                                break
                        if switch:
                            neighbor_list.append(neighbor)
                elif neighbor[0] == coord[0]:
                    x1, y1 = coord
                    x2, y2 = neighbor
                    min_y = min([y1, y2])
                    max_y = max([y1, y2])
                    switch = True
                    for inter in intersect:
                        x3, y3 = inter
                        if x3 == x2 and min_y<y3<max_y:
                            switch=False
                            break
                    if switch:
                        neighbor_list.append(neighbor)
                elif neighbor[1] == coord[1]:
                    x1, y1 = coord
                    x2, y2 = neighbor
                    min_x = min([x1, x2])
                    max_x = max([x1, x2])
                    switch = True
                    for inter in intersect:
                        x3, y3 = inter
                        if y3 == y2 and min_x < x3 < max_x:
                            switch = False
                            break
                    if switch:
                        neighbor_list.append(neighbor)
        return neighbor_list

    def add_neighbor(self, neighbor):
        if neighbor not in self.neighbors:
            self.neighbors.append(neighbor)

    def setParent(self, node):
        self.parent = node

    def get_coord(self):
        return self.coord

    def potentialNeighbor(self):
        x, y = self.coord
        if x % 1 == 0 and y % 1 == 0:
            return [(x - 1, y), (x - 1, y - 1), (x, y - 1), (x + 1, y + 1), (x + 1, y), (x, y + 1), (x + 1, y - 1),
                    (x - 1, y + 1)]
        elif x % 1 == 0:
            if y > 0:
                y = int(y)
            else:
                y = int(y) - 1
            return [(x, y), (x, y + 1), (x + 1, y), (x + 1, y + 1), (x - 1, y), (x - 1, y + 1)]
        elif y % 1 == 0:
            if x > 0:
                x = int(x)
            else:
                x = int(x) - 1
            return [(x, y), (x + 1, y), (x, y + 1), (x + 1, y + 1), (x, y - 1), (x + 1, y - 1)]
        else:
            if y > 0:
                y = int(y)
            else:
                y = int(y) - 1
            if x > 0:
                x = int(x)
            else:
                x = int(x) - 1
            return [(x, y), (x + 1, y), (x, y + 1), (x + 1, y + 1)]

    def get_neighbor(self):
        return self.neighbors

    def get_val(self):
        return self.val
