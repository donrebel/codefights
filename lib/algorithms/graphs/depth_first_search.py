from data_structures.graph import Graph

class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0

    def dfs(self):
        for vertex in self:
            vertex.set_color('white')
            vertex.set_pred(-1)
        for vertex in self:
            if vertex.get_color() == 'white':
                self.dfs_visit(vertex)

    def dfs_visit(self, start_vertex):
        start_vertex.set_color('gray')
        self.time += 1
        start_vertex.set_discover_time(self.time)
        for v in start_vertex.get_connections():
            if v.get_color() == 'white':
                v.set_pred(start_vertex)
                self.dfs_visit(v)
        self.time += 1
        start_vertex.set_finish_time(self.time)
        start_vertex.set_color('black')


