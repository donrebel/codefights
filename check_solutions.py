def swapLexOrder(str_, pairs):
    n = len(str_)
    str_ = list(str_)

    corr = [set() for _ in range(n)]
    nodes = set()
    for a, b in pairs:
        corr[a-1].add(b-1)
        corr[b-1].add(a-1)
        nodes.add(a-1)
        nodes.add(b-1)

    while nodes:
        active = {nodes.pop()}
        group = set()
        while active:
            group |= active
            nodes -= active
            active = {y for x in active for y in corr[x] if y in nodes}

        chars = iter(sorted((str_[i] for i in group), reverse=True))
        for i in sorted(group):
            str_[i] = next(chars)

    return "".join(str_)




def countClouds(skyMap):
    nodes = set()
    corr = [set() for _ in range(len(skyMap) * len(skyMap[0]))]
    for i in range(len(skyMap)):
        for j in range(len(skyMap[i])):
            x = skyMap[i][j]
            if x == '1':
                get_valid_steps((i, j), skyMap, corr, nodes)
    res = []
    while nodes:
        active = {nodes.pop()}
        group = set()
        while active:
            group |= active
            nodes -= active
            active = {y for x in active for y in corr[x] if y in nodes}
        res.append(group)
    return len(res)

def get_valid_steps(c, map, corr, nodes):
    l = len(map)
    m = len(map[0])
    steps = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    a = c[0] * m + c[1]
    for s in steps:
        step = (c[0] + s[0], c[1] + s[1])
        if 0 <= step[0] < l and 0 <= step[1] < m and map[step[0]][step[1]] == '1':
            b = step[0] * m + step[1]
            corr[a].add(b)
            corr[b].add(a)
            nodes.add(b)
    nodes.add(a)


skyMap = [['0', '1', '1', '0', '1'],
          ['0', '1', '1', '1', '1'],
          ['0', '0', '0', '0', '1'],
          ['1', '0', '0', '1', '1']]

print(countClouds(skyMap)) # = 2;

skyMap = [['0', '1', '0', '0', '1'],
          ['1', '1', '0', '0', '0'],
          ['0', '0', '1', '0', '1'],
          ['0', '0', '1', '1', '0'],
          ['1', '0', '1', '1', '0']]

print(countClouds(skyMap)) # = 5;



def nearestGreater(a):
    pass

a = [1, 4, 2, 1, 7, 6]
print(nearestGreater(a)) #= [1, 4, 1, 2, -1, 4].

