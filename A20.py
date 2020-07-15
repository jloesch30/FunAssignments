import os

class Queue (object):
    def __init__ (self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue (self, item):
        self.queue.append (item)

    # remove an item from the beginning of the queue
    def dequeue (self):
        return (self.queue.pop(0))

    # check if the queue is empty
    def is_empty (self):
        return (len (self.queue) == 0)

    # return the size of the queue
    def size (self):
        return (len (self.queue))

class Stack (object):
    def __init__ (self):
            self.stack = []

    # add an item to the top of the stack
    def push (self, item):
        self.stack.append (item)

    # remove an item from the top of the stack
    def pop (self):
        return self.stack.pop()

    # check the item on the top of the stack
    def peek (self):
        return self.stack[-1]

    # check if the stack if empty
    def is_empty (self):
        return (len (self.stack) == 0)

    # return the number of elements in the stack
    def size (self):
        return (len (self.stack))

class Vertex (object):
    def __init__ (self, label):
        self.label = label
        self.visited = False

    # determine if a vertex was visited
    def was_visited (self):
        return self.visited

    # determine the label of the vertex
    def get_label (self):
        return self.label

    # string representation of the vertex
    def __str__ (self):
        return str (self.label)

class Graph (object):
    # constructor
    def __init__(self):
        self.Vertices = []
        self.adjMat = []
    # check if a vertex is already in the graph
    def has_vertex (self, label):
        nVert = len (self.Vertices)
        for i in range (nVert):
            if (label == (self.Vertices[i]).get_label()):
                return True
        return False
    # get the index from the vertex label
    def get_index (self, label):
        nVert = len (self.Vertices)
        for i in range (nVert):
            if (label == (self.Vertices[i]).get_label()):
                return i
        return -1
    # add a Vertex object with a given label to the graph
    def add_vertex (self, label):
        if (not self.has_vertex (label)):
            self.Vertices.append (Vertex (label))
        
        # add a new column in the adjacency matrix
        nVert = len (self.Vertices)
        for i in range (nVert - 1):
            (self.adjMat[i]).append (0)

        # add a new row for the new vertex
        new_row = []
        for i in range (nVert):
            new_row.append (0)
        self.adjMat.append (new_row)
    # display the adj_matrix
    def get_matrix (self):
        print('Adjacency Matrix')
        for row in self.adjMat:
            for col in row:
                print(col, end = ' ')
            print()
        print()
    # add weighted directed edge to graph
    def add_directed_edge (self, start, finish, weight = 1):
        self.adjMat[start][finish] = weight
    # add weighted undirected edge to graph
    def add_undirected_edge (self, start, finish, weight = 1):
        self.adjMat[start][finish] = weight
        self.adjMat[finish][start] = weight
    # get edge weight between two vertices
    # return -1 if edge does not exist
    def get_edge_weight (self, fromVertexLabel, toVertexLabel):
        start = self.get_index(fromVertexLabel)
        fin = self.get_index(toVertexLabel)
        try:
            return self.adjMat[start][fin]
        # does not exist
        except:

            return -1
    # get a list of immediate neighbors that you can go to from a vertex
    # return a list of indices or an empty list if there are none
    def get_neighbors (self, vertexLabel):
        # find the row (idx) of vertexLabel
        v = self.get_index(vertexLabel)
        neighbors = []
        vertices = self.get_vertices()
        # find verts connected to label
        for i in range(len(vertices)):
            if self.adjMat[v][i] > 0:
                neighbors.append(i)
        return neighbors
    # return an index to an unvisited vertex adjacent to vertex v (index)
    def get_adj_unvisited_vertex (self, v):
        nVert = len (self.Vertices)
        for i in range (nVert):
            if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):
                return i
        return -1
    # get a copy of the list of Vertex objects
    def get_vertices (self):
        return self.Vertices
    # do a depth first search in a graph starting at vertex v (index)
    def dfs (self, v):
        # create the Stack
        theStack = Stack ()

        # mark the vertex v as visited and push it on the Stack
        (self.Vertices[v]).visited = True
        print (self.Vertices[v])
        theStack.push (v)

        # visit all the other vertices according to depth
        while (not theStack.is_empty()):
        # get an adjacent unvisited vertex
            u = self.get_adj_unvisited_vertex (theStack.peek())
            if (u == -1):
                u = theStack.pop()
            else:
                (self.Vertices[u]).visited = True
                print (self.Vertices[u])
                theStack.push (u)

        # the stack is empty, reset the flags
        nVert = len (self.Vertices)
        for i in range (nVert):
            (self.Vertices[i]).visited = False

    # do a breadth first search in a graph starting at vertex v (index)
    def bfs (self, v):
        q = Queue()
        q.enqueue(v)
        self.Vertices[v].visited = True

        while not q.is_empty():
            vert = q.dequeue() # dequeue a vertex object
            print(self.Vertices[vert].get_label())

            label = self.Vertices[vert].get_label()
            vert_neighbors = self.get_neighbors(label)
            for neighbor in vert_neighbors:
                if not self.Vertices[neighbor].was_visited():
                    q.enqueue(neighbor)
                    self.Vertices[neighbor].visited = True
    
    def bfs_shortestPath (self, start, finish):
        paths = []
        q = Queue()
        s = self.get_index(start)
        q.enqueue(self.Vertices[s])
        self.Vertices[s].visited = True
        
        while not q.is_empty():
            vert = q.dequeue() # dequeue a vertex object
            new_path = []
            if len(paths) == 0:
                # start
                new_path.append(vert)
                paths.append(new_path)
            # find the neigbors of the dequeued element
            label = self.Vertices[vert].get_label()
            vert_neighbors = self.get_neighbors(label)
            for neighbor in vert_neighbors:
                if not self.Vertices[neighbor].was_visited():
                    new_path = []
                     
                    q.enqueue(neighbor)
                    self.Vertices[neighbor].visited = True

    # delete an edge from the adjacency matrix
    # delete the edge if the graph is going from start to finish
    def delete_edge (self, fromVertexLabel, toVertexLabel):
        start = self.get_index(fromVertexLabel)
        fin = self.get_index(toVertexLabel)

        self.adjMat[start][fin] = 0
        self.adjMat[fin][start] = 0
    # delete a vertex from the vertex list and all edges from and
    # to it in the adjacency matrix
    def delete_vertex (self, vertexLabel):
        idx = self.get_index(vertexLabel)
        self.Vertices.pop(idx)
        # delete the row
        del self.adjMat[idx]
        # delete column
        sum(map(lambda x: x.pop(idx), self.adjMat))

def main():
    # create the graph
    cities = Graph()

    # open file
    in_file = open(r'C:\Users\Owner\Desktop\graph.txt', 'r')

    # add the cities to graph
    num_verts = int ((in_file.readline()).strip())

    # print ('num of verts is', num_verts)
    # add vertices to the graph
    for _ in range (num_verts):
        city = (in_file.readline()).strip()
        # print (city)
        cities.add_vertex (city)

    # read num of edges
    num_edges = int ((in_file.readline()).strip())
    # print ('num of edges is:', num_edges)

    # add edges to matrix
    for _ in range (num_edges):
        edge = (in_file.readline()).strip()
        # print (edge)
        edge = edge.split()
        start = int (edge[0])
        finish = int (edge[1])
        weight = int (edge[2])
        
        cities.add_directed_edge (start, finish, weight)

    # test depth first search
    print('Depth First Search')
    start = (in_file.readline()).strip()
    start_idx = cities.get_index(start)
    # start_idx_dfs = 9
    cities.dfs (start_idx)
    # spacer
    print()
    # test breadth first search
    print('Breadth First Search')
    cities.bfs (start_idx)
    # spacer
    print()
    # test shortest path
    print('Getting the shortest path')
    labelStart = 'Los Angeles'
    labelEnd = 'Miami'
    cities.bfs_shortestPath(labelStart, labelEnd)
    # print the shortest path
    
    # test deletion of an edge
    del_edge = (in_file.readline().strip()).split(' ')
    start_label = del_edge[0]
    fin_label = del_edge[1]
    print('Deletion of an edge')
    cities.delete_edge( start_label, fin_label)
    print()
    cities.get_matrix()
    # test vertex delete
    del_city = in_file.readline().strip()
    cities.delete_vertex(del_city)
    print()
    print('Deletion of a vertex')
    print()
    print('List of Vertices')
    verts = cities.get_vertices()
    for v in verts:
        print(v)
    print()
    cities.get_matrix()
    

main()
