# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        pointer = dummy

        while pointer.next and pointer.next.next:
            firstNode = pointer.next
            secondNode = pointer.next.next

            firstNode.next = secondNode.next
            secondNode.next = firstNode
            pointer.next = secondNode

            pointer = firstNode

        return dummy.next