import functools

# make a WUG class (weighted, undirected Graph)
class WUG():
    def __init__(self):
        self.vertex_list = []
        self.vertex_dict = {} # vertex -> list of vertices
        self.edge_count = 0

    def __str__(self):
        V = self.vertex_list
        E = [[v1, v2] \
                for v1, edges in self.vertex_dict.items() \
                for v2 in edges]
        return 'V: {}\nE: {}\n'.format(V, E)

    # finds wheter vertex is the vertex of the graph
    def isVertex(self,vertex):
        if vertex in self.vertex_list:
            return True
        return False

    # return the number of the vertexs
    def vertexCount(self):
        return len(self.vertex_list)

    # return the number of the edges
    def edgeCount(self):
        return self.edge_count

    # return the list of the Vertex
    def getVertices(self):
        return self.vertex_list

    # add the Vertex in WUG
    def addVertex(self, vertex):
        self.vertex_list.append(vertex)
        self.vertex_dict[vertex] = {}

    # remove the Vertex in WUG
    def removeVertex(self, vertex):

        # Check wheter vertes is the vertex of the Graph
        if not self.isVertex(vertex):
            print("Not in a vertex list!")
            return

        # remove vertex in the vertexlist and the vertex_dict
        self.vertex_list.remove(vertex)
        for v2 in self.vertex_dict[vertex]:
            del self.vertex_dict[v2][vertex]
            self.edge_count -= 1
            v2.degree -= 1
        del self.vertex_dict[vertex]

    # add Edge in the graph
    def addEdge(self, v1, v2, weight):
        if not (self.isVertex(v1) and self.isVertex(v2)):
            print("Error")
            return
        self.vertex_dict[v1][v2] = weight
        self.vertex_dict[v2][v1] = weight
        v1.degree += 1
        v2.degree += 1
        self.edge_count += 1

    # return the degree of the vertex
    def degree(self, vertex):
        assert self.isVertex(vertex)
        if not self.isVertex(vertex):
            print("Not in a vertex list")
            return
        return vertex.degree

    # return the lsit of the neighbors of the vertex
    def getNeighbors(self, vertex):
        return list(self.vertex_dict[vertex].keys())

    # remove the Edge of the Graph
    def removeEdge(self, v1, v2):
        if not self.isVertex(v1) or not self.isVertex(v2):
            print("Not a vertex")
            return
        if not self.isEdge(v1,v2):
            print("Not connected!")
            return
        v1.degree -= 1
        v2.degree -= 1
        self.edge_count -= 1
        del self.vertex_dict[v1][v2]
        del self.vertex_dict[v2][v1]

    # check whether two vertices are connected or not
    def isEdge(self, v1, v2):
        if v2 in self.vertex_dict[v1]:
            if v1 in self.vertex_dict[v2]:
                return True
        return False

    # define the weight of the two vertices
    def weight(self, v1, v2):
        if not self.isEdge(v1,v2):
            print("Not connected")
            return False
        return self.vertex_dict[v1][v2]


# define a class of the Vertex
class Vertex():
    def __init__(self, name):
        self.name = name
        self.degree = 0

    def __repr__(self):
        return '%s' %self.name

# define a class of the Edge
class Edge():
    def __init__(self, v1, v2, weight):
        self.v1 = v1
        self.v2 = v2
        self.weight = weight

# define a depth first search
def DFS(graph):
    found = {} # dict that contains the vertex that visited
    wug = WUG()
    # function for recursive proceed
    def DFS_inner(vertex):
        wug.addVertex(vertex)
        found[vertex] = True
        for v in graph.getNeighbors(vertex):
            if not v in found:
                DFS_inner(v)
                wug.addEdge(vertex, v, 1)

    # check wheter the graph is empty or not
    try:
        vertex = graph.getVertices()[0]
    except:
        print('Empty graph!')
        return
    else:
        DFS_inner(vertex)
        return wug

# define a breadth first search
# using a queue and find the tree
def BFS(graph):
    queue = []
    found = {}
    wug = WUG()
    start_ver = graph.getVertices()[0]
    wug.addVertex(start_ver)
    queue.append(start_ver)
    found[start_ver] = True

    while len(queue) > 0:
        vertex = queue.pop(0)
        for v in graph.getNeighbors(vertex):
            if not v in found:
                wug.addVertex(v)
                wug.addEdge(vertex, v, 1)
                found[v] = True
                queue.append(v)

    return wug


if __name__ == '__main__':
    filename = input("File name : ")
    tree_format = input("DFS or BFS: ")
    with open(filename,'r') as f:
        try:
            exec(f.read())
            if not 'wug' in locals():
                raise SyntaxError
        except:
            print('invalid file format')
        else:
            if tree_format == 'DFS':
                print(DFS(wug))
            elif tree_format == 'BFS':
                print(BFS(wug))
            else:
                print('invalid tree format')

