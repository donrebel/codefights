class BinaryTree:
    def __init__(self, root_node):
        self.key = root_node
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, new_node):
        if self.leftChild is None:
            self.leftChild = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.insertLeft(self.leftChild)
            self.leftChild = t

    def insertRight(self, new_node):
        if self.rightChild is None:
            self.rightChild = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.insertRight(self.rightChild)
            self.rightChild = t

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def setRootVal(self, root_node):
        self.key = root_node

    def getRootVal(self):
        return self.key

from stack import Stack
import operator
def build_parse_tree(fpexp):
    fplist = fpexp.split(' ')
    st = Stack()
    e_tree = BinaryTree('')
    st.push(e_tree)
    current_three = e_tree
    for i in fplist:
        if i == '(':
            current_three.insertLeft('')
            st.push(current_three)
            current_three = current_three.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            current_three.setRootVal(int(i))
            parent = st.pop()
            current_three = parent
        elif i in ['+', '-', '*', '/']:
            current_three.setRootVal(i)
            current_three.insertRight('')
            st.push(current_three)
            current_three = current_three.getRightChild()
        elif i == ')':
            current_three = st.pop()
        else:
            raise ValueError
    return e_tree

class BTreeParser:
    def preorder(self, b_tree):
        if b_tree:
            print(b_tree.getRootVal())
            self.preorder(b_tree.getLeftChild())
            self.preorder(b_tree.getRightChild())

    def postorde(self, b_tree):
        if b_tree:
            self.preorder(b_tree.getLeftChild())
            self.preorder(b_tree.getRightChild())
            print(b_tree.getRootVal())

    def inorder(self, b_tree):
        if b_tree:
            self.preorder(b_tree.getLeftChild())
            print(b_tree.getRootVal())
            self.preorder(b_tree.getRightChild())

def postordereval(tree):
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
    if tree:
        res1 = postordereval(tree.getLeftChild())
        res2 = postordereval(tree.getRightChild())
        if res1 and res2:
            return opers[tree.getRootVal()](res1, res2)
        else:
            return tree.getRootVal()

def printexp(tree):
  sVal = ""
  if tree:
      sVal = '(' + printexp(tree.getLeftChild())
      sVal = sVal + str(tree.getRootVal())
      sVal = sVal + printexp(tree.getRightChild())+')'
  return sVal

if __name__ == '__main__':
    bt = build_parse_tree("( ( 10 + 5 ) * 3 )")
    print(postordereval(bt))
    print(printexp(bt))