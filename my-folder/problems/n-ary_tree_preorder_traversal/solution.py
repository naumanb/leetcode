"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution(object):

# Solution: Recursively traverse through the tree and add the node value to the list

    def preorder(self, root):
        if not root: # if node doesn't exist, return nothing
            return []
        nodeVals = [] # store values of nodes in preorder traversal
        nodeVals.append(root.val) # add root node value
        for child in root.children:
            nodeVals.extend(self.preorder(child)) # recursively traverse through children nodes
        return nodeVals