from sys import maxsize
from data_structures.graph import Graph
from data_structures.priority_queue import PriorityQueue

def prim(aGraph, start):
    pq = PriorityQueue()
    for v in aGraph:
        v.set_distance(maxsize)
        v.set_pred(None)
    start.set_distance(0)
    pq.build_heap([(v, v.get_distance()) for v in aGraph])
    while not pq.is_empty():
        current_vert = pq.dequeue()[0]
        for next_vert in current_vert.get_connections():
            new_cost = current_vert.get_weight(next_vert)
            if next_vert in pq and new_cost < next_vert.get_distance():
                next_vert.set_distance(new_cost)
                next_vert.set_pred(current_vert)
                pq.decrease_priority(next_vert, new_cost)

if __name__ == '__main__':
    g = Graph()
    g.add_edge('u', 'v', 2)
    g.add_edge('u', 'x', 1)
    g.add_edge('u', 'w', 5)
    g.add_edge('v', 'w', 3)
    g.add_edge('v', 'x', 2)
    g.add_edge('x', 'w', 3)
    g.add_edge('x', 'y', 1)
    g.add_edge('y', 'w', 1)
    g.add_edge('w', 'z', 5)
    g.add_edge('y', 'z', 1)

    prim(g, g.get_vertex('u'))
    print(g.get_path('w'))