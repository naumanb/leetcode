"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        oldToCopy = {None: None}
        ptr = head
        while ptr:
            copy = Node(ptr.val)
            oldToCopy[ptr] = copy
            ptr = ptr.next
        ptr = head
        while ptr:
            copy = oldToCopy[ptr]
            copy.next = oldToCopy[ptr.next]
            copy.random = oldToCopy[ptr.random]
            ptr = ptr.next
        return oldToCopy[head]