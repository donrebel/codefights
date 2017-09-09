class QuickFindUF:

    def __init__(self, n):
        self.id = []
        self.size = n
        for i in range(self.size):
            self.id.append(i)

    def connected(self, p, q):
        return self.id[p] == self.id[q]

    def union(self, p, q):
        pid = self.id[p]
        qid = self.id[q]
        for i in range(self.size):
            if self.id[i] == pid:
                self.id[i] = qid


class QuickUnionUF:

    def __init__(self, n):
        self.id = []
        for i in range(n):
            self.id.append(i)

    def root(self, i):
        while i != self.id[i]:
            i = self.id[i]
        return i

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        rp = self.root(p)
        rq = self.root(q)
        self.id[rp] = rq


class WeightedQuickUnionUF:

    def __init__(self, n):
        self.id = []
        self.sz = {}
        for i in range(n):
            self.id.append(i)

    def root(self, i):
        while i != self.id[i]:
            i = self.id[i]
        return i

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        rp = self.root(p)
        rq = self.root(q)
        if rp != rq:
            if not(rp in self.sz.keys()):
                self.sz[rp] = 0
            if not(rq in self.sz.keys()):
                self.sz[rq] = 0

            if self.sz[rp] < self.sz[rq]:
                self.id[rp] = rq
                self.sz[rq] += self.sz[rp]
            else:
                self.id[rq] = rp
                self.sz[rp] += self.sz[rq]


class WeightedQuickUnionWithCompressionUF:

    def __init__(self, n):
        self.id = []
        self.sz = {}
        for i in range(n):
            self.id.append(i)

    def root(self, i):
        while i != self.id[i]:
            self.id[i] = self.id[self.id[i]]
            i = self.id[i]
        return i

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        rp = self.root(p)
        rq = self.root(q)
        if rp != rq:
            if not (rp in self.sz.keys()):
                self.sz[rp] = 0
            if not (rq in self.sz.keys()):
                self.sz[rq] = 0

            if self.sz[rp] < self.sz[rq]:
                self.id[rp] = rq
                self.sz[rq] += self.sz[rp]
            else:
                self.id[rq] = rp
                self.sz[rp] += self.sz[rq]


# def run(inp):
#     ar = inp[:]
#     n = len(ar)
#     uf = UF(n)
#     while len(ar) > 0:
#         p = ar.pop()
#         q = ar.pop()
#         if (not uf.connected(p, q)):
#             uf.union(p, q)
#             print(p + ' ' + q)

if __name__ == '__main__':
    a = {}
    if 1 in a.keys():
        print(a[1])
    else:
        print(1)