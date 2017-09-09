from data_structures.binary_heap import BinHeap


class PriorityQueue:
    def __init__(self):
        self.bh = BinHeap()

    def enqueue(self, item):
        if self.bh.is_empty():
            self.bh.build_heap([item])
        else:
            self.bh.insert(item)

    def build_heap(self, alist):
        self.bh.build_heap(alist)

    def dequeue(self):
        return self.bh.del_min()

    def decrease_priority(self, key, priority):
        self.bh.decrease_priority(key, priority)

    def is_empty(self):
        return self.bh.is_empty()

    def size(self):
        return self.bh.size()

    def __contains__(self, item):
        return item in self.bh

if __name__ == '__main__':
    pq = PriorityQueue()
    pq.enqueue(10)
    pq.enqueue(4)
    pq.enqueue(8)
    pq.enqueue(15)

    print(pq.dequeue())
    print(pq.dequeue())
    print(pq.dequeue())
    print(pq.dequeue())

