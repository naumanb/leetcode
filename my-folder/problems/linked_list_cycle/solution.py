# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Create a hash set to keep track of nodes already indexed
        hashset = set()
        while head:
            if head in hashset: #if current node already was indexed before, there must be a cycle
                return True
            else:
                hashset.add(head) #if node wasn't indexed, add it to hashset
                head = head.next
        return False