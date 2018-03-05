# Definition for singly-linked list.
from node import UnorderedList


def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """

    if l1.isEmpty() and l1.isEmpty():
        return UnorderedList()

    if l1.isEmpty():
        return l2

    if l2.isEmpty():
        return l1
    carry = 0
    ret = UnorderedList()

    while not l1.isEmpty() or not l2.isEmpty():

        item1 = l1.pop()
        item2 = l2.pop()
        carry = carry + item1 + item2
        ret.add(carry % 10)
        carry = carry // 10

    l4 = UnorderedList()
    while not ret.isEmpty():
        l4.add(ret.pop())

    return l4


# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

l1 = UnorderedList()
l1.add(3)
l1.add(4)
l1.add(2)
l2 = UnorderedList()
l2.add(4)
l2.add(6)
l2.add(5)
l3 = addTwoNumbers(l1, l2)

while not l3.isEmpty():
    print(l3.pop())
