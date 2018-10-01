class Graph:
    def __init__(self):
        self.vertices = []
        self.distances = {}
    def addVertex(self, node):
        self.vertices.append(node)
    def addEdge(node1, node2, weight):
        self.distances[(node1, node2)] = weight;
        self.distances[(node2, node1)] = weight;
    def getDistance(node1, node2):
        return self.distance[(node1, node2)]
        
class Queue: 
    def __init__(self):
        self.head = None
    def enqueue(node, val):
        node.setVal(val)
        if (self.head == None):
            self.head = node
        elif (self.head.next == None):
            if(self.head.val < node.val):
                node.next = self.head
                self.head = node
            else:
                self.head.next = node
        else:
            prev = None
            ptr = self.head
            while (ptr != None):
                if (ptr.val>node.val):
                    if (prev == None):
                        node.next = self.head
                        self.head = node
                    else:
                        prev.next = node
                        node.next = ptr
                prev = ptr
                ptr = ptr.next
            if(ptr == None):
                prev.next = node
    def dequeue():
        reval = self.head
        if(self.head == None):
            return None
        elif(self.head.next == None):
            self.head = None
        else:
            self.head = self.head.next
            reval.next = None
        return self.head
    def isEmpty():
        if(self.head == None): return true
        else: return false
    def isInQueue(node):
    
            
class Node:
    def __init__(self, name):
        self.name = name
        self.next = None
        self.val = None
    def setVal(val):
        self.val = val
    def setNeighbor(neighbors)
        self.neighbors = neighbors
    def setParent(node)
        self.parent = node