# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        ptr = head
        vals = []

        while ptr:
            vals.append(ptr.val)
            ptr = ptr.next

        vals.sort()

        ptr = head
        for val in vals:
            ptr.val = val
            ptr = ptr.next

        return head