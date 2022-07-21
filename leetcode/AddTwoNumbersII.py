# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head): #reverseList(self, head: ListNode) -> ListNode:
        last = None
        while head:
            # keep the next node
            tmp = head.next
            # reverse the link
            head.next = last
            # update the last node and the current node
            last = head
            head = tmp
        
        return last
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # reverse lists
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)
        
        head = None
        carry = 0
        while l1 or l2:
            # get the current values 
            x1 = l1.val if l1 else 0
            x2 = l2.val if l2 else 0
            
            # current sum and carry
            val = (carry + x1 + x2) % 10
            carry = (carry + x1 + x2) // 10
            
            # update the result: add to front
            curr = ListNode(val)
            curr.next = head
            head = curr
            
            # move to the next elements in the lists
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry:
            curr = ListNode(carry)
            curr.next = head
            head = curr

        return head        