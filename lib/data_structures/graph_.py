from sys import maxsize

class Vertex:
    def __init__(self, key):
        self.id = key
        self.connected_to = {}
        self.distance = maxsize
        self.color = 'white'
        self.predecessor = None
        self.discover_time = 0
        self.finish_time = 0
        self.visited = False

    def set_distance(self, v):
        self.distance = v

    def get_distance(self):
        return self.distance

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_pred(self, vert):
        self.predecessor = vert

    def get_pred(self):
        return self.predecessor

    def set_discover_time(self, time):
        self.discover_time = time

    def get_discover_time(self):
        return self.discover_time

    def set_finish_time(self, time):
        self.finish_time = time

    def get_finish_time(self):
        return self.finish_time

    def add_neighbor(self, nbr, weight=0):
        self.connected_to[nbr] = weight

    def get_connections(self):
        return self.connected_to.keys()

    def get_id(self):
        return self.id

    def get_weight(self, nbr):
        return self.connected_to[nbr]

    def __str__(self):
        return str(self.id) + ' connected to ' + str([x.id for x in self.connected_to])

class Graph:
    def __init__(self):
        self.vert_list = {}
        self.num_vertices = 0

    def add_vertex(self, key):
        self.num_vertices += 1
        new_vertex = Vertex(key)
        self.vert_list[key] = new_vertex
        return new_vertex

    def get_vertex(self, key):
        if key in self.vert_list:
            return self.vert_list[key]
        else:
            return None

    def __contains__(self, key):
        return key in self.vert_list

    def add_edge(self, f, t, cost=0):
        if f not in self.vert_list:
            nv = self.add_vertex(f)
        if t not in self.vert_list:
            nv = self.add_vertex(t)
        self.vert_list[f].add_neighbor(self.vert_list[t], cost)

    def get_vertices(self):
        return self.vert_list.keys()

    def __iter__(self):
        return iter(self.vert_list.values())

    def __str__(self):
        return str([str(x) for x in self.vert_list])

    def get_path(self, key):
        res = []
        current_vert = self.get_vertex(key)
        while current_vert.get_pred() is not None:
            res.append(current_vert.get_id())
            current_vert = current_vert.get_pred()
        res.append(current_vert.get_id())
        return res

if __name__ == '__main__':
    g = Graph()
    for i in range(6):
        g.add_vertex(i)
    print(g.vert_list)

    g.add_edge(0,1,5)
    g.add_edge(0,5,2)
    g.add_edge(1,2,4)
    g.add_edge(2,3,9)
    g.add_edge(3,4,7)
    g.add_edge(3,5,3)
    g.add_edge(4,0,1)
    g.add_edge(5,4,8)
    g.add_edge(5,2,1)

    for v in g:
        for w in v.get_connections():
            print("(%s, %s)" % (v.get_id(), w.get_id()))



