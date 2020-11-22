
class Graph():
    """A graph class, which lets you add nodes and edges."""
    def __init__(self):
        # Nodes is a list 
        self.nodes_ = []
        # Edges is a dictionary. If (x,y) exists, then
        # edges_[x --> y] = 1
        self.edges_ = {}

    def AddNode(self, name):
        self.nodes_.append(name)

    def AddEdge(self, src, dest):
        self.edges_[src + " --> " + dest] = 1

    def DeleteEdge(self, src, dest):
        self.edges_.pop(src + " --> " + dest, None)

    def Print(self):
        print("Curr graph")
        for edge in self.edges_.keys():
            print(edge)



# Create a graph 
g = Graph()
# Add nodes
g.AddNode("A")
g.AddNode("B")
g.AddNode("C")
# Add edges 
g.AddEdge("A", "B")
g.AddEdge("B", "C")
# Print
g.Print()
# remove A --> B
g.DeleteEdge("A", "B")
g.Print()
    
