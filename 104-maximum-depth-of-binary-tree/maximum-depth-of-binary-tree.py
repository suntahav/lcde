# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            #empty tree so no height
            return 0
        
        if (root.left is None) and (root.right is None):
            #edge node so return 1
            return 1
        
        if root.left is None:
            #only right height needed plus root
            return 1 + self.maxDepth(root.right)
        elif root.right is None:
            #only left height needed plus root
            return 1 + self.maxDepth(root.left)
        else:
            #max of left or right height plus root
            return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))