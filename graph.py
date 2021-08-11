class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbours = []

class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = []
        
    
    def insertVertex(self, vertex):
        self.vertices.append(vertex)

    def insertEdge(self, a, b):
        if b not in a.neighbours:
            a.neighbours.append(b)

        if a not in b.neighbours:
            b.neighbours.append(a)

        self.edges.append((a,b))

graph = Graph()
a = Vertex("A")
b = Vertex("B")
c = Vertex("C")
d = Vertex("D")
e = Vertex("E")

graph.insertVertex(a)
graph.insertVertex(b)
graph.insertVertex(c)
graph.insertVertex(d)
graph.insertVertex(e)

graph.insertEdge(a,c)
graph.insertEdge(a,d)
graph.insertEdge(d,b)
graph.insertEdge(b,e)
graph.insertEdge(d,e)


print(graph.vertices)
print(graph.edges)
print(len(a.neighbours))
print(len(b.neighbours))
print(len(c.neighbours))
print(len(d.neighbours))
print(len(e.neighbours))


