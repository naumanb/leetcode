# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def trimBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: TreeNode
        """
        if not root:
            return None
        if root.val < low: # if the current node is less than the lower bound, return the right subtree
            return self.trimBST(root.right, low, high)
        if root.val > high: # if the current node is greater than the upper bound, return the left subtree
            return self.trimBST(root.left, low, high)
        root.left = self.trimBST(root.left, low, high) 
        root.right = self.trimBST(root.right, low, high) 
        return root 