from data_structures.queue import Queue

class Node:
    def __init__(self, key):
        self.id = key
        self.visited = False
        self.connected_to = {}

    def get_connections(self):
        return self.connected_to

    def add_connection(self, n, weight):
        self.connected_to[n] = weight

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, key):
        n = Node(key)
        self.nodes[key] = n
        return n

    def get_node(self, key):
        return self.nodes[key]

    def add_edge(self, f, t, weight=0):
        if f not in self.nodes:
            nf = self.add_node(f)
        if t not in self.nodes:
            nt = self.add_node(t)
        self.nodes[f].add_connection(self.nodes[t], weight)


def visit(node):
    print(node.id)

def search_dfs(root):  #DFS
    if root is not None:
        visit(root)
        root.visited = True
        for n in root.get_connections():
            if not n.visited:
                search_bfs(n)

def search_bfs(start_node):
    q = Queue()
    q.enqueue(start_node)
    while not q.is_empty():
        n = q.dequeue()
        if not n.visited:
            visit(n)
            n.visited = True
            for i in n.get_connections():
                q.enqueue(i)

# ================================================================================
# Given a directed graph, design an algorithm to find out whether there is a route
# between two nodes.
def find_path(graph, start_val, end_val):
    ns = graph.get_node(start_val)
    ne = graph.get_node(end_val)
    q = Queue()
    q.enqueue(ns)
    found = False
    while not q.is_empty() and not found:
        n = q.dequeue()
        for c in n.get_connections():
            if not c.visited:
                if c == ne:
                    found = True
                else:
                    q.enqueue(c)
        n.visited = True
    return found


if __name__ == '__main__':

    g = Graph()
    g.add_edge(0, 1, 5)
    g.add_edge(0, 5, 2)
    g.add_edge(1, 2, 4)
    g.add_edge(3, 4, 7)
    g.add_edge(3, 5, 3)
    g.add_edge(4, 0, 1)
    g.add_edge(5, 4, 8)
    g.add_edge(5, 2, 1)

    root = g.get_node(0)
    print(find_path(g, 5, 1))




class Node(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None


def minValueNode(node):
    current = node
    while (current.left is not None):
        current = current.left
    return current


def maxValueNode(node):
    current = node
    while current.right is not None:
        current = current.right
    return current


def insert(node, value):
    if node is None:
        return Node(value)
    if value < node.value:
        node.left = insert(node.left, value)
    else:
        node.right = insert(node.right, value)
    return node


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.value)
        inorder(root.right)


def deleteNode(root, value):
    if root is None:
        return root
    if value < root.value:
        root.left = deleteNode(root.left, value)
    elif (value > root.value):
        root.right = deleteNode(root.right, value)
    else:
        if root.left is None and root.right is None:
            root = None
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = maxValueNode(root.left)
        root.value = temp.value
        root.left = deleteNode(root.left, temp.value)
    return root


# =================================
def deleteT(t,v):
    if v==t.value:
        if t.left:
            if t.left.right:
                q=t.left
                while q.right.right:
                    q=q.right
                t.value=q.right.value
                q.right=q.right.left
                return t
            else:
                t.left.right=t.right
                return t.left
        else:
            return t.right
    if v<t.value:
        if t.left:
            t.left=deleteT(t.left,v)
    else:
        if t.right:
            t.right=deleteT(t.right,v)
    return t

def deleteFromBST(t, q):
    for i in q:
        if not t:
            break
        t=deleteT(t,i)
    return t



import random

class TreapNode:
    def __init__(self, key, data, priority=None):
        self.key = key
        self.data = data
        # self.priority = priority if priority is not None else random.random()
        self.priority = random.random()
        self.size = 1
        self.cnt = 1
        self.parent = None
        self.left = None
        self.right = None

    def left_rotate(self):
        a = self
        b = a.right
        a.right = b.left
        b.left = a
        a = b
        b = a.left
        b.size = b.left_size() + b.right_size() + b.cnt
        a.size = a.left_size() + a.right_size() + a.cnt
        return a

    def right_rotate(self):
        a = self
        b = a.left
        a.left = b.right
        b.right = a
        a = b
        b = a.right
        b.size = b.left_size() + b.right_size() + b.cnt
        a.size = a.left_size() + a.right_size() + a.cnt
        return a

    def left_size(self):
        return 0 if self.left is None else self.left.size

    def right_size(self):
        return 0 if self.right is None else self.right.size

    def __repr__(self):
        return '<node key:%s ran:%f size:%d left:%s right:%s>' % (str(self.key), self.priority, self.size, str(self.left), str(self.right))


class Treap:
    def __init__(self):
        self.root = None

    def _insert(self, node, key, data=None, priority=None):
        if node is None:
            return TreapNode(key, data, priority)

        node.size += 1
        if key < node.key:
            node.left = self._insert(node.left, key, data, priority)
            if node.left.priority < node.priority:
                node = node.right_rotate()
            # node.left.parent = node
        else:
            node.right = self._insert(node.right, key, data, priority)
            if node.right.priority < node.priority:
                node = node.left_rotate()
            # node.right.parent = node
        return node

    def insert(self, key, data=None, priority=None):
        self.root = self._insert(self.root, key, data, priority)

    def __repr__(self):
        return str(self.root)

    def _traverse(self, node, callback):
        if node is None:
            return
        self._traverse(node.left, callback)
        callback(node)
        self._traverse(node.right, callback)

    def traverse(self, callback):
        self._traverse(self.root, callback)



a = [1, 4, 2, 1, 7, 6]
t = Treap()
for i, x in enumerate(a):
    t.insert(x, i)



def trv(node):
    print(node.key, node.data)

t.traverse(trv)




def nearestGreater(a):
    res = []
    def fmax(enum):
        res = []
        stack = []
        for i, x in enum:
            while stack and x >= a[stack[-1]]:
                stack.pop()
            res.append(stack[-1] if stack else -1)
            stack.append(i)
        return res

    enum = list(enumerate(a))
    lmas = fmax(enum)
    rmas = fmax(enum[::-1])[::-1]
    for ix, (l,r) in enumerate(zip(lmas, rmas)):
        if l == -1 or abs(ix - r) < abs(ix - l):
            res.append(r)
        else:
            res.append(l)
    return res


# a = [1, 4, 2, 1, 7, 6]
# print(nearestGreater(a))


# a = [2, 1, 2, 1, 2]
# print(nearestGreater(a)) #= [-1, 0, -1, 2, -1] [1, 4, 1, 2, -1, 4]




