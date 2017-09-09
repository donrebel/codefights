from sys import maxsize

# =============================================
# Note: Try to solve this task in O(n) time using O(1) additional space, where n is the number of elements in the list,
# since this is what you'll be asked to do during an interview.
#
# Given a singly linked list of integers l and an integer k, remove all elements from list l that have
# a value equal to k.
#
# Example
#
# For l = [3, 1, 2, 3, 4, 5] and k = 3, the output should be
# removeKFromList(l, k) = [1, 2, 4, 5];
# For l = [1, 2, 3, 4, 5, 6, 7] and k = 10, the output should be
# removeKFromList(l, k) = [1, 2, 3, 4, 5, 6, 7].

def removeKFromList(l, k):
    if l is None:
        return None
    n = l
    prev = None
    while n is not None:
        if n.value == k and prev is not None:
            prev.next = n.next
        else:
            prev = n
        n = n.next
    if l.value == k:
        res = l.next
        l.next = None
    else:
        res = l
    return res
# =============================================
# Note: Try to solve this task in O(n) time using O(1) additional space, where n is the number of elements in l,
# since this is what you'll be asked to do during an interview.
#
# Given a singly linked list of integers, determine whether or not it's a palindrome.
#
# Example
#
# For l = [0, 1, 0], the output should be
# isListPalindrome(l) = true;
# For l = [1, 2, 2, 3], the output should be
# isListPalindrome(l) = false.

def isListPalindrome(l):
    slow = l
    fast = l
    st = []
    while fast is not None and fast.next is not None:
        st.append(slow.value)
        slow = slow.next
        fast = fast.next.next
    if fast is not None:
        slow = slow.next
    ar_l = len(st)
    while slow is not None:
        top = st[ar_l - 1]
        if slow.value != top:
            return False
        slow = slow.next
        ar_l = ar_l - 1
    return True
# =======================================
# You're given 2 huge integers represented by linked lists. Each linked list element is a number from 0 to 9999
# that represents a number with exactly 4 digits. The represented number might have leading zeros. Your task is to add
# up these huge integers and return the result in the same format.
#
# Example
#
# For a = [9876, 5432, 1999] and b = [1, 8001], the output should be
# addTwoHugeNumbers(a, b) = [9876, 5434, 0].
#
# Explanation: 987654321999 + 18001 = 987654340000.
#
# For a = [123, 4, 5] and b = [100, 100, 100], the output should be
# addTwoHugeNumbers(a, b) = [223, 104, 105].


# recursive solutions

def addTwoHugeNumbersRecursive(a, b):
    # return addTwoHugeNumbersReversOrder(a, b)
    return addTwoHugeNumbersNaturalOrder(a, b)

def addTwoHugeNumbersReversOrder(l1, l2, carry=0):
    if carry == 0 and l1 is None and l2 is None:
        return None

    value = carry
    if l1 is not None:
        value += l1.value

    if l2 is not None:
        value += l2.value

    res = LinkedListNode(value % 10)

    if l1 is not None or l2 is not None:
        more = addTwoHugeNumbersReversOrder(
            None if l1 is None else l1.next, None if l2 is None else l2.next, 1 if value >= 10 else 0)
        res.next = more
    return res


class PartialSum:
    def __init__(self, node, carry=0):
        self.node = node
        self.carry = carry


def addTwoHugeNumbersNaturalOrder(l1, l2):
    ln1 = len(l1)
    ln2 = len(l2)
    if ln1 > ln2:
        l2 = pad_list(l2, ln1 - ln2)
    else:
        l1 = pad_list(l1, ln2 - ln1)

    res = sum_helper(l1, l2)
    if res.carry > 0:
        t = LinkedListNode(res.carry)
        t.next = res.node
        res.node = t

    return res.node

def sum_helper(l1, l2):
    if l1 is None and l2 is None:
        return PartialSum(LinkedListNode(None), 0)

    prev_step_res = sum_helper(l1.next, l2.next)

    step_sum = prev_step_res.carry + l1.value + l2.value
    res_node = LinkedListNode(step_sum % 10)
    if prev_step_res.node.value is not None:
        res_node.next = prev_step_res.node
    step_res = PartialSum(res_node, 1 if step_sum >= 10 else 0)
    return step_res

def pad_list(l, length):
    n = l
    for i in range(length):
        t = LinkedListNode(0)
        t.next = n
        n = t
    return n

# Iterative solution
def addTwoHugeNumbers(l1, l2):
    ln1 = len(l1)
    ln2 = len(l2)
    if ln1 > ln2:
        l2 = pad_list(l2, ln1 - ln2)
    else:
        l1 = pad_list(l1, ln2 - ln1)

    res = sum_hlp(get_tail(l1), get_tail(l2))
    return res

def sum_hlp(a, b):
    l1 = a
    l2 = b
    carry = 0
    n = None
    while l1 is not None and l2 is not None:
        step_sum = carry + l1.value + l2.value
        step_res = step_sum % 10000
        carry = 1 if step_sum >= 10000 else 0
        t = LinkedListNode(step_res)
        t.next = n
        n = t
        l1 = l1.prev
        l2 = l2.prev
    if carry != 0:
        t = LinkedListNode(carry)
        t.next = n
        n = t
    return n

def get_tail(l):
    n = l
    prev = None
    while n is not None:
        n.prev = prev
        prev = n
        n = n.next
    return prev

# =======================================
# Note: Your solution should have O(l1.length + l2.length) time complexity, since this is what you will be asked to
# accomplish in an interview.
# Given two singly linked lists sorted in non-decreasing order, your task is to merge them. In other words,
# return a singly linked list, also sorted in non-decreasing order, that contains the elements from both original lists.
#
# Example
#
# For l1 = [1, 2, 3] and l2 = [4, 5, 6], the output should be
# mergeTwoLinkedLists(l1, l2) = [1, 2, 3, 4, 5, 6];
# For l1 = [1, 1, 2, 4] and l2 = [0, 3, 5], the output should be
# mergeTwoLinkedLists(l1, l2) = [0, 1, 1, 2, 3, 4, 5]

def mergeTwoLinkedLists(l1, l2):
    if l1 is None or l1.value is None:
        return l2
    res = LinkedListNode()
    pointer = res
    while l1 is not None or l2 is not None:
        v1 = maxsize
        v2 = maxsize
        if l1 is not None:
            v1 = l1.value
        if l2 is not None:
            v2 = l2.value
        v = min(v1, v2)
        if pointer.value is None:
            pointer.value = v
        else:
            n = LinkedListNode(v)
            pointer.next = n
            pointer = pointer.next
        if v == v1:
            l1 = l1.next
        else:
            l2 = l2.next
    return res

# =======================================
# Given a linked list l, reverse its nodes k at a time and return the modified list. k is a positive integer that
#  is less than or equal to the length of l. If the number of nodes in the linked list is not a multiple of k,
#  then the nodes that are left out at the end should remain as-is.
# You may not alter the values in the nodes - only the nodes themselves can be changed.

def reverseNodesInKGroups(l, k):
    start = None
    runner = l
    prev_tail = None
    while runner is not None:
        step_counter = 0
        local_head = None
        local_tail = None
        origin_head = runner
        while runner is not None and step_counter < k:
            n = LinkedListNode(runner.value)
            if step_counter == 0:
                local_tail = n
            n.next = local_head
            local_head = n
            runner = runner.next
            step_counter += 1
        if start is None:
            start = local_head
        if prev_tail is not None:
            if step_counter <= k - 1:
                prev_tail.next = origin_head
            else:
                prev_tail.next = local_head
        prev_tail = local_tail
    return start


# =======================================
# Given a singly linked list of integers l and a non-negative integer n, move the last n list nodes to the beginning
# of the linked list.

def rearrangeLastN(l, n):
    if n == 0:
        return l
    first_runner = l
    start = l
    step_counter = 0
    while first_runner is not None and step_counter < n:
        first_runner = first_runner.next
        step_counter += 1
    second_runner = l
    if first_runner is None:
        return l
    while first_runner.next is not None:
        first_runner = first_runner.next
        second_runner = second_runner.next
    last_el = first_runner
    res = second_runner.next
    second_runner.next = None
    if last_el is not None:
        last_el.next = start
    return res

# =======================================
# Definition for singly-linked list:
class LinkedListNode(object):
    def __init__(self, x=None):
        self.value = x
        self.next = None

    @classmethod
    def build(cls, ar):
        res = cls()
        n = res
        for x in ar:
            if res.value == None:
                res.value = x
            else:
                t = cls(x)
                n.next = t
                n = t
        return res

    def __len__(self):
        res = 0
        n = self
        while n is not None:
            res += 1
            n = n.next
        return res

    def __repr__(self):
        n = self
        res = []
        while n is not None:
            res.append(n.value)
            n = n.next
        return str(res)

    def __str__(self):
        return self.__repr__()

    def __eq__(self, other):
        return str(self) == str(other)


# =========================================
l = [3, 1, 2, 3, 4, 5]
k = 3
assert removeKFromList(LinkedListNode.build(l), k) == LinkedListNode.build([1, 2, 4, 5])
l = [1, 2, 3, 4, 5, 6, 7]
k = 10
assert removeKFromList(LinkedListNode.build(l), k) == LinkedListNode.build([1, 2, 3, 4, 5, 6, 7])

l = [0, 1, 0]
assert isListPalindrome(LinkedListNode.build(l)) == True
l = [1, 2, 2, 3]
assert isListPalindrome(LinkedListNode.build(l)) == False


l1 = LinkedListNode.build([9876, 5432, 1999])
l2 = LinkedListNode.build([1, 8001])
assert addTwoHugeNumbers(l1, l2) == LinkedListNode.build([9876, 5434, 0])
l1 = LinkedListNode.build([123, 4, 5])
l2 = LinkedListNode.build([100, 100, 100])
assert addTwoHugeNumbers(l1, l2) == LinkedListNode.build([223, 104, 105])


l = LinkedListNode.build([1, 2, 3, 4, 5])
k = 2
assert reverseNodesInKGroups(l, k) == LinkedListNode.build([2, 1, 4, 3, 5])
l = LinkedListNode.build([1, 2, 3, 4, 5])
k = 1
assert reverseNodesInKGroups(l, k) == LinkedListNode.build([1, 2, 3, 4, 5])
l = LinkedListNode.build([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
k = 3
assert reverseNodesInKGroups(l, k) == LinkedListNode.build([3, 2, 1, 6, 5, 4, 9, 8, 7, 10, 11])


l = LinkedListNode.build([1, 2, 3, 4, 5])
n = 3
assert rearrangeLastN(l, n) == LinkedListNode.build([3, 4, 5, 1, 2])



l = LinkedListNode.build([1, 2, 3, 4, 5, 6, 7])
n = 1
assert rearrangeLastN(l, n) == LinkedListNode.build([7, 1, 2, 3, 4, 5, 6])