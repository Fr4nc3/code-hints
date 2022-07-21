def solution(inputString):
    
    return inputString == inputString[::-1]
    # arr = list(inputString)
    # n = len(arr)
    # head = arrayToList(inputString, n)
    # print(head)
    # return isPalindrome(head)


def arrayToList(arr, n):
    root = None
    for i in range(0, n, 1):
        root = insert(root, arr[i])
        
def insert(root, item):
    temp = Node(item)
      
    if (root == None):
        root = temp
    else :
        ptr = root
        while (ptr.next != None):
            ptr = ptr.next
        ptr.next = temp
      
    return root

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

def isPalindrome(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    vals = []
    current_node = head
    while current_node is not None:
        vals.append(current_node.val)
        current_node = current_node.next
    print(vals)
    print(vals[::-1])
    return vals == vals[::-1]
