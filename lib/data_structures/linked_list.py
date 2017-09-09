class LinkedListNode():
    def __init__(self, val=None):
        self.key = val
        self.next = None

    def append(self, val):
        if self.key is None:
            self.key = val
        else:
            t = LinkedListNode(val)
            n = self
            while n.next is not None:
                n = n.next
            n.next = t

    def __len__(self):
        n = self
        length = 0
        while n is not None:
            length += 1
            n = n.next
        return length

    def __str__(self):
        r = ''
        n = self
        while n is not None:
            r += str(n.key) + ', '
            n = n.next
        return r

    def __iter__(self):
        n = self
        while n is not None:
            yield n
            n = n.next

if __name__ == '__main__':
    l = LinkedListNode()
    for i in range(10):
        l.append(i)

    print(l)
    print(len(l))

    for i in l:
        print(i.key)
