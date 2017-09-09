from collections import defaultdict

class Graph:
    def __init__(self, v, type='directed'):
        self.type = type
        self.size = v
        self.graph = defaultdict(set)
        self.vertices = range(self.size)
        self.time = 0

    def add_edge(self, u, v):  # function to add edge
        if self.type == 'directed':  # if graph is directed
            self.graph[u].add(v)
        else:
            self.graph[u].add(v)
            self.graph[v].add(u)


def build_graph(connections):
    g = Graph(len(connections), 'directed')
    for v, c in enumerate(connections):
        for u in c:
            g.add_edge(v, u)
    return g


def graph_traversal(g):
    colors = [0] * g.size

    def dfs(node, res):
        if colors[node] == 0:
            res.append(node)
            colors[node] = 1
            for x in g.graph[node]:
                if colors[x] == 1:
                    continue
                else:
                    dfs(x, res)
            colors[node] = 2

    res = []
    for x in g.vertices:
        dfs(x, res)
    print(res)


connections = [[1], [2], [3, 4], [4], [0]]
g = build_graph(connections)


from collections import defaultdict




'''A recursive function that finds and prints bridges
using DFS traversal
u --> The vertex to be visited next
visited[] --> keeps tract of visited vertices
disc[] --> Stores discovery times of visited vertices
parent[] --> Stores parent vertices in DFS tree'''

def bridgeUtil(g, u, visited, parent, low, discover_time, res):

    # Count of children in current node
    children = 0

    # Mark the current node as visited and print it
    visited[u] = True

    # Initialize discovery time and low value
    discover_time[u] = g.time
    low[u] = g.time
    g.time += 1

    # Recur for all the vertices adjacent to this vertex
    for v in g.graph[u]:
        # If v is not visited yet, then make it a child of u
        # in DFS tree and recur for it
        if visited[v] == False:
            parent[v] = u
            children += 1
            bridgeUtil(g, v, visited, parent, low, discover_time, res)

            # Check if the subtree rooted with v has a connection to
            # one of the ancestors of u
            low[u] = min(low[u], low[v])

            ''' If the lowest vertex reachable from subtree
            under v is below u in DFS tree, then u-v is
            a bridge'''
            if low[v] > discover_time[u]:
                print("%d %d" % (u, v))
                res.append((u, v))


        elif v != parent[u]:  # Update low value of u for parent function calls.
            low[u] = min(low[u], discover_time[v])

# DFS based function to find all bridges. It uses recursive
# function bridgeUtil()
def bridge(g):

    # Mark all the vertices as not visited and Initialize parent and visited,
    # and ap(articulation point) arrays
    visited = [False] * (g.size)
    discover_time = [float("Inf")] * (g.size)
    low = [float("Inf")] * (g.size)
    parent = [-1] * (g.size)
    res = []
    # Call the recursive helper function to find bridges
    # in DFS tree rooted with vertex 'i'
    for i in range(g.size):
        if visited[i] == False:
            bridgeUtil(g, i, visited, parent, low, discover_time, res)
    return res


# g1 = Graph(5, 'undirected')
# g1.add_edge(1, 0)
# g1.add_edge(0, 2)
# g1.add_edge(2, 1)
# g1.add_edge(0, 3)
# g1.add_edge(3, 4)
#
# bridge(g1)


# connections = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
connections = [[0, 1, 1, 1, 0, 0], [1, 0, 1, 0, 0, 0], [1, 1, 0, 0, 0, 0], [1, 0, 0, 0, 1, 1], [0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0]]
g = Graph(len(connections), 'undirect')
for v, c in enumerate(connections):
    for u, cs in enumerate(c):
        if cs == 1:
            g.add_edge(v, u)


print(bridge(g))


min1 = 10
min2_10 = 1
min11 = 2
s = 22


def phoneCall(min1, min2_10, min11, s):
    cnt = 0
    while s > 0:
        if cnt == 0:
            s -= min1
        elif cnt >= 1 and cnt < 10:
            s -= min2_10
        else:
            s -= min11
        cnt += 1
    if s < 0:
        cnt -= 1
    return cnt

print(phoneCall(min1, min2_10, min11, s)) # = 14.