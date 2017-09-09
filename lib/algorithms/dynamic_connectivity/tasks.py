import random
import datetime
from data_structures import WeightedQuickUnionWithCompressionUF

def question1(n, m):
    user_ids = []
    friend_log = []
    timestamp = datetime.datetime(2017, 1, 1)

    for i in range(n):
        user_ids.append(i)
    for i in range(m):
        friend_log.append({'f': random.randrange(n), 'b': random.randrange(n), 'timestamp': timestamp})
        timestamp += datetime.timedelta(seconds=random.randrange(60))

    uf = WeightedQuickUnionWithCompressionUF(n)
    num_roots = n
    i = 0
    res_t = None
    all_connected = False
    while i < m and not all_connected:
        f = friend_log[i]['f']
        b = friend_log[i]['b']
        t = friend_log[i]['timestamp']
        if not uf.connected(f, b):
            uf.union(f, b)
            num_roots -= 1
            if num_roots == 1:
                all_connected = True
                res_t = t
        i += 1
    return res_t

if __name__ == '__main__':
    for i in range(10):
        print(question1(25, 75))

