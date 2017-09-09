from data_structures.queue import Queue

class Node:
    def __init__(self, key):
        self.id = key
        self.visited = False
        self.connected_to = {}

    def get_connections(self):
        return self.connected_to

    def add_connection(self, n, weight):
        self.connected_to[n] = weight

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, key):
        n = Node(key)
        self.nodes[key] = n
        return n

    def get_node(self, key):
        return self.nodes[key]

    def add_edge(self, f, t, weight=0):
        if f not in self.nodes:
            nf = self.add_node(f)
        if t not in self.nodes:
            nt = self.add_node(t)
        self.nodes[f].add_connection(self.nodes[t], weight)


def visit(node):
    print(node.id)

def search_dfs(root):  #DFS
    if root is not None:
        visit(root)
        root.visited = True
        for n in root.get_connections():
            if not n.visited:
                search_bfs(n)

def search_bfs(start_node):
    q = Queue()
    q.enqueue(start_node)
    while not q.is_empty():
        n = q.dequeue()
        if not n.visited:
            visit(n)
            n.visited = True
            for i in n.get_connections():
                q.enqueue(i)

# ================================================================================
# Given a directed graph, design an algorithm to find out whether there is a route
# between two nodes.
def find_path(graph, start_val, end_val):
    ns = graph.get_node(start_val)
    ne = graph.get_node(end_val)
    q = Queue()
    q.enqueue(ns)
    found = False
    while not q.is_empty() and not found:
        n = q.dequeue()
        for c in n.get_connections():
            if not c.visited:
                if c == ne:
                    found = True
                else:
                    q.enqueue(c)
        n.visited = True
    return found


if __name__ == '__main__':

    g = Graph()
    g.add_edge(0, 1, 5)
    g.add_edge(0, 5, 2)
    g.add_edge(1, 2, 4)
    g.add_edge(3, 4, 7)
    g.add_edge(3, 5, 3)
    g.add_edge(4, 0, 1)
    g.add_edge(5, 4, 8)
    g.add_edge(5, 2, 1)

    root = g.get_node(0)
    print(find_path(g, 5, 1))
