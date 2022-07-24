# 25. Reverse Nodes in k-Group
# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

# You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

# Example 1:


# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]
# Example 2:


# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]
 

# Constraints:

# The number of nodes in the list is n.
# 1 <= k <= n <= 5000
# 0 <= Node.val <= 1000
 

# Follow-up: Can you solve the problem in O(1) extra memory space?

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        headNode = head
        # Base condition
        if headNode is None or k == 1:
            return headNode
        # Dummy node before headNode
        dummy = ListNode(-1)
        # Point the next of this dummy node to the current headNode
        dummy.next = headNode
        # Node to keep track of the previous node
        previous = dummy
        # Variable to keep count of the nodes in the linked list
        count = 0
        # Reference to the headNode which will be used to traverse
        current = headNode
        # Loop for all the nodes in the list
        while current is not None:
            count += 1
            if count % k == 0:
                previous = self.reverseList(previous, current.next)
                current = previous.next
            else:
                current = current.next
        return dummy.next

    def reverseList(self, start, end):
        previous = start.next
        current = previous.next
        while current is not end:
            nextNode = current.next
            current.next = start.next
            start.next = current
            current = nextNode
        previous.next = end
        return previous