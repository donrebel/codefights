from data_structures.graph import Graph

def knight_graph(board_size):
    kt_graph = Graph()
    for row in range(board_size):
        for col in range(board_size):
            node_id = pos_to_node_id(row, col, board_size)
            new_positions = gen_legal_moves(row, col, board_size)
            for e in new_positions:
                n_id = pos_to_node_id(e[0], e[1], board_size)
                kt_graph.add_edge(node_id, n_id)
    return kt_graph


def pos_to_node_id(row, col, board_size):
    return row * board_size + col


def gen_legal_moves(x, y, board_size):
    new_moves = []
    move_offset = [(-1, -2), (-1, 2), (-2, -1), (-2, 1), (1, -2), (1, 2), (2, -1), (2, 1)]
    for i in move_offset:
        new_x = x + i[0]
        new_y = y + i[1]
        if legal_coord(new_x, board_size) and legal_coord(new_y, board_size):
            new_moves.append((new_x, new_y))
    return new_moves


def legal_coord(x, size):
    if 0 <= x < size:
        return True
    else:
        return False

def knight_tour(n, path, u, limit):
    u.set_color('gray')
    path.append(u)
    print(str(n) + ' : ' + str([x.get_id() for x in path]))
    if n < limit:
        # nbr_list = list(u.get_connections())
        nbr_list = list(order_by_avail(u))
        i = 0
        done = False
        while i < len(nbr_list) and not done:
            if nbr_list[i].get_color() == 'white':
                done = knight_tour(n + 1, path, nbr_list[i], limit)
            i = i + 1
        if not done:
            path.pop()
            u.set_color('white')
    else:
        done = True
    return done

# optimization
def order_by_avail(n):
    res_list = []
    for v in n.get_connections():
        if v.get_color() == 'white':
            c = 0
            for w in v.get_connections():
                if w.get_color() == 'white':
                    c = c + 1
            res_list.append((c, v))
    res_list.sort(key=lambda x: x[0])
    return [y[1] for y in res_list]

if __name__ == '__main__':
    g = knight_graph(8)
    knight_tour(0, [], g.get_vertex(2), 63)