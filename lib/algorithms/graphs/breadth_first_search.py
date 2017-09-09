from data_structures.graph import Graph
from data_structures.queue import Queue

def build_graph(w_list):
    d = {}
    g = Graph()
    for word in w_list:
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i + 1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]

    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.add_edge(word1, word2)
    return g

def bfs(g, start):
    start.set_distance(0)
    start.set_pred(None)
    vq = Queue()
    vq.enqueue(start)
    while vq.size() > 0:
        current_vert = vq.dequeue()
        for nbr in current_vert.get_connections():
            if nbr.get_color() == 'white':
                nbr.set_color('gray')
                nbr.set_distance(current_vert.get_distance() + 1)
                nbr.set_pred(current_vert)
                vq.enqueue(nbr)
        current_vert.set_color('black')

def traverse(v):
    x = v
    while x.get_pred():
        print(x.get_id())
        x = x.get_pred()
    print(x.get_id())


if __name__ == '__main__':
    wl = ['pope', 'rope', 'nope', 'hope', 'lope', 'mope', 'cope', 'pipe', 'pape', 'pole', 'role', 'pore', 'pose', 'poke', 'pops']
    g = build_graph(wl)
    bfs(g, g.get_vertex('pope'))
    traverse(g.get_vertex('role'))
