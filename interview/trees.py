from data_structures.linked_list import LinkedListNode
from sys import maxsize

class Node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children

    def __str__(self, level=0):
        ret = '\t' * level + repr(self.value) + '\n'
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret


class BinaryTree:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self, level=0):
        ret = '\t' * level + repr(self.data) + '\n'
        if self.left:
            ret += self.left.__str__(level + 1)
        if self.right:
            ret += self.right.__str__(level + 1)
        return ret

    def insert_left(self, v):
        if self.left is None:
            self.left = BinaryTree(v)

        else:
            t = BinaryTree(v)
            t.left = self.left
            self.left = t
        self.left.parent = self
        return self.left

    def insert_right(self, v):
        if self.right is None:
            self.right = BinaryTree(v)
        else:
            t = BinaryTree(v)
            t.right = self.right
            self.right = t
        self.right.parent = self
        return self.right

    def get_root_val(self):
        return self.data

    def set_root_val(self, v):
        self.data = v

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def get_node(self, key):
        if key is None:
            return None
        return self._preorder_traversal(self, key)

    def _preorder_traversal(self, tree, key):
        if tree:
            if tree.get_root_val() == key:
                return tree
            elif tree.get_root_val() > key:
                return self._preorder_traversal(tree.get_left_child(), key)
            elif tree.get_root_val() < key:
                return self._preorder_traversal(tree.get_right_child(), key)




def action(v):
    print(v)

def preorder_traversal(tree):
    if tree:
        action(tree.get_root_val())
        preorder_traversal(tree.get_left_child())
        preorder_traversal(tree.get_right_child())

def inorder_traversal(tree):
    if tree:
        inorder_traversal(tree.get_left_child())
        action(tree.get_root_val())
        inorder_traversal(tree.get_right_child())

def postorder_traversal(tree):
    if tree:
        postorder_traversal(tree.get_left_child())
        postorder_traversal(tree.get_right_child())
        action(tree.get_root_val())

# ==========================================================
# Implement a function to check if a binary tree is balanced. For the purposes of this
# question, a balanced tree is defined to be a tree such that the heights of the two
# subtrees of any node never differ by more than one
def is_balanced_1(itree):  # not optimal O(N2)
    def get_height(tree):
        if tree is None:
            return 0
        else:
            return max(get_height(tree.get_left_child()), get_height(tree.get_right_child())) + 1

    def _is_balanced(tree):
        if tree is None:
            return True
        heigh_diff = get_height(tree.get_left_child()) - get_height(tree.get_right_child())
        if abs(heigh_diff) > 1:
            return False
        else:
            return _is_balanced(tree.get_left_child()) and _is_balanced(tree.get_right_child())

    return _is_balanced(itree)


def is_balanced_2(itree): # optimal
    def get_height(tree):
        if tree is None:
            return 0
        else:
            height_left = get_height(tree.get_left_child())
            if height_left == -1:
                return -1
            height_right = get_height(tree.get_right_child())
            if height_right == -1:
                return -1

            heigh_diff = height_left - height_right
            if abs(heigh_diff) > 1:
                return -1
            else:
                return max(height_left, height_right) + 1

    def _is_balanced(tree):
        if get_height(tree) == -1:
            return False
        else:
            return True

    return _is_balanced(itree)


# Given a sorted (increasing order) array with unique integer elements, write an algorithm to create a binary
# search tree with minimal height
def create_minimal_bst(list, first_i, last_i):
    if last_i < first_i:
        return None
    mid_i = (first_i + last_i) // 2
    n = BinaryTree(list[mid_i])
    n.left = create_minimal_bst(list, first_i, mid_i - 1)
    # parent link is optional
    if n.left:
        n.left.parent = n
    n.right = create_minimal_bst(list, mid_i + 1, last_i)
    if n.right:
        n.right.parent = n
    return n

def biuld_bst_tree(list):
    return create_minimal_bst(list, 0, len(list) - 1)


# Given a binary tree, design an algorithm which creates a linked list of all the nodes at
# each depth (e.g., if you have a tree with depth D,you'll have D linked lists
def create_level_linked_list(node, lists, level):
    if node is None:
        return None
    if len(lists) == level:
        list = LinkedListNode()
        lists.append(list)
    else:
        list = lists[level]
    list.append(node.get_root_val())
    create_level_linked_list(node.get_left_child(), lists, level + 1)
    create_level_linked_list(node.get_right_child(), lists, level + 1)

def build_level_linkeb_list_dfs(node):
    lists = []
    create_level_linked_list(node, lists, 0)
    return lists

def build_level_linked_list_bfs(node):
    res = []
    current = LinkedListNode()
    if node is not None:
        current.append(node)
    while len(current) > 0:
        res.append(current)
        parents = current
        current = LinkedListNode()
        for parent in parents:
            if parent.key is not None:
                if parent.key.get_left_child() is not None:
                    current.append(parent.key.get_left_child())
                if parent.key.get_right_child() is not None:
                    current.append(parent.key.get_right_child())
    return res


# Implemen t a function to check if a binary tree isa binary search tree
def checkBST(node):
    return _checkBST(node, -maxsize, maxsize)

def _checkBST(n, min, max):
    if n is None:
        return True
    if n.get_root_val() <= min or max < n.get_root_val():
        return False
    if (not _checkBST(n.get_left_child(), min, n.get_root_val())) or (not _checkBST(n.get_right_child(), n.get_root_val(), max)):
        return False
    return True

# Write an algorithm to find the 'next' node (i.e., in-order successor) of a given node in
# a binary search tree. You may assume that each node has a link to its parent

def get_left_most_child(n):
    if n is None:
        return None
    while n.get_left_child() is not None:
        n = n.get_left_child()
    return n

def get_inorder_successor(n):
    if n is None:
        return None
    if n.get_right_child() is not None:
        return get_left_most_child(n.get_right_child())
    else:
        c = n
        p = c.parent
        while p is not None and p.get_left_child() != c:
            c = p
            p = p.parent
        return p


# Design an algorithm and write code to find the first common ancestor of
# two nodes in a binary tree. Avoid storing additional nodes in a data
# structure. NOTE: This is not necessarily a binary search tree.

def covers(root, cn):
    if root is None:
        return False
    if root == cn:
        return True
    return covers(root.left, cn) or covers(root.right, cn)

def common_ancestor_helper(root, n1, n2):
    if root is None:
        return None
    if root == n1 or root == n2:
        return root

    is_n1_on_left = covers(root.left, n1)
    is_n2_on_left = covers(root.left, n2)

    if is_n1_on_left != is_n2_on_left:
        return root

    if is_n1_on_left:
        child_side = root.left
    else:
        child_side = root.right

    return common_ancestor_helper(child_side, n1, n2)

def common_ancestor(root, n1, n2):
    if not covers(root, n1) or not covers(root, n2):
        return None
    return common_ancestor_helper(root, n1, n2)

# Optimized solution
class Result:
    def __init__(self, n, is_anc):
        self.node = n
        self.is_ancestor = is_anc


def common_ancestor_helper_2(root, n1, n2):
    if root is None:
        return Result(None, False)
    if root == n1 and root == n2:
        return Result(root, True)

    res_l = common_ancestor_helper_2(root.left, n1, n2)
    if res_l.is_ancestor:
        return res_l
    res_r = common_ancestor_helper_2(root.right, n1, n2)
    if res_r.is_ancestor:
        return res_r

    if res_l.node is not None and res_r.node is not None:
        return Result(root, True)
    elif root == n1 or root == n2:
        if res_l.node is not None or res_r.node is not None:
            is_ancestor = True
        else:
            is_ancestor = False
        return Result(root, is_ancestor)
    else:
        res_node = res_l.node if res_l.node is not None else res_r.node
        return Result(res_node, False)


def common_ancestor_2(root, n1, n2):
    r = common_ancestor_helper_2(root, n1, n2)
    if r.is_ancestor:
        return r.node
    return None


# You have two very large binary trees: Tl, with millions of nodes, and T2, with
# hundreds of nodes. Create an algorithm to decide if T2 is a subtree of Tl.
# A tree T2 is a subtree of Tl if there exists a node n in T1 such that
# the subtree of n is identical to T2. That is, if you cut off the tree at
# node n, the two trees would be identical.


def contains_tree(t1, t2):
    if t2 is None:
        return True
    sub_tree(t1, t2)


def sub_tree(t1, t2):
    if t1 is None:
        return False
    if t1.data == t2.data:
        if match_tree(t1, t2):
            return True
    return sub_tree(t1.left, t2) or sub_tree(t1.right, t2)


def match_tree(t1, t2):
    if t2 is None and t2 is None:
        return True
    if t1 is None or t2 is None:
        return False

    if t1.data != t2.data:
        return False

    return match_tree(t1.left, t2.left) and match_tree(t1.right, t2.right)

# You are given a binary tree in which each node contains a value. Design an algorithm to print all paths which sum to
# a given value. The path does not need to start or end at the root or a leaf

def _find_sum(node, sum, path, level):
    if node is None:
        return
    path[level] = node.data
    t = 0
    for i in range(level, -1, -1):
        t += path[i]
        if t == sum:
            prnt(path, i, level)

    _find_sum(node.left, sum, path, level + 1)
    _find_sum(node.right, sum, path, level + 1)
    path[level] = None

def find_sum(node, sum):
    path = [None] * depth(node)
    _find_sum(node, sum, path, 0)

def prnt(path, start, end):
    res = ''
    for i in range(start, end + 1):
        res += str(path[i]) + ' '
    print(res)

def depth(node):
    if node is None:
        return 0
    else:
        return 1 + max(depth(node.left), depth(node.right))







if __name__ == '__main__':
    # nt = Node(2)
    # nt.children = [Node(5)]
    # nt.children[0].children = [Node(7), Node(1)]
    # nt.children[0].children[1].children = [Node(9), Node(0)]
    # nt.children[0].children[0].children = [Node(6)]
    # nt.children[0].children[0].children[0].children = [Node(3)]
    # nt.children[0].children[0].children[0].children[0].children = [Node(8)]
    # nt.children[0].children[0].children[0].children[0].children[0].children = [Node(4)]
    #
    # print(nt)

    t = BinaryTree(2)
    n8 = t.insert_right(8)
    n5 = t.insert_left(5)
    n7 = n5.insert_left(7)
    # n1 = n5.insert_right(1)
    # n9 = n1.insert_left(9)
    # n0 = n1.insert_right(0)
    # n6 = n7.insert_left(6)
    # n3 = n6.insert_left(3)
    # n8 = n3.insert_left(8)
    # n4 = n8.insert_left(4)

    bst = biuld_bst_tree([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(bst)

    n1 = bst.get_node(8)
    n2 = bst.get_node(6)
    print(find_sum(bst, 22))


