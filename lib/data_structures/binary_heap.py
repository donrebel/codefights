# BinHeap item: (key, priority)
class BinHeap:
    def __init__(self):
        self.heap_list = []
        self.current_size = 0

    def size(self):
        return self.current_size

    def is_empty(self):
        return self.current_size == 0

    def build_heap(self, alist):
        i = len(alist) // 2
        self.current_size = len(alist)
        self.heap_list = [(None, 0)] + alist[:]
        while i > 0:
            self.perc_down(i)
            i = i - 1

    def perc_down(self, i):
        while i * 2 <= self.current_size:
            mc = self.min_child(i)
            if self.heap_list[i][1] > self.heap_list[mc][1]:
                temp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[mc]
                self.heap_list[mc] = temp
            i = mc

    def min_child(self, i):
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i * 2][1] < self.heap_list[i * 2 + 1][1]:
                return i * 2
            else:
                return i * 2 + 1

    def insert(self, val):
        self.heap_list.append(val)
        self.current_size += 1
        self.perc_up(self.current_size)

    def perc_up(self, i):
        while i > 0:
            if self.heap_list[i][1] < self.heap_list[i // 2][1]:
                tmp = self.heap_list[i // 2]
                self.heap_list[i // 2] = self.heap_list[i]
                self.heap_list[i] = tmp
            i = i // 2

    def del_min(self):
        res = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.heap_list.pop()
        self.perc_down(1)
        return res

    def decrease_priority(self, key, priority):
        i = 1
        while (i < self.current_size) and not (self.heap_list[i][0] == key):
            i = i + 1
        if self.heap_list[i][0] == key:
            temp = (key, priority)
            self.heap_list[i] = temp
            self.perc_up(i)

    def __contains__(self, item):
        i = 0
        found = False
        while i <= self.current_size and not found:
            if self.heap_list[i][0] == item:
                found = True
            i = i + 1
        return found

if __name__ == '__main__':
    bh = BinHeap()
    bh.build_heap([('b', 2), ('a', 1), ('c', 3), ('e', 5), ('d', 4), ('f', 6)])

    bh.decrease_priority('d', 2)

    print(bh.del_min())
    print(bh.del_min())
    print(bh.del_min())
    print(bh.del_min())
    print(bh.del_min())