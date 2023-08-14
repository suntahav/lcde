# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEqual(self, root, subRoot):
        if (root is None) and (subRoot is None):
            return True
        
        if (root is not None) and (subRoot is None):
            return False
        
        if (root is None) and (subRoot is not None):
            return False

        if root.val == subRoot.val:
            left = self.checkEqual(root.left, subRoot.left)
            right = self.checkEqual(root.right, subRoot.right)
            if left and right:
                return True
            else:
                return False
        else:
            return False
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if (root is None) and (subRoot is None):
            return True
        
        if root is None:
            return False
        
        if root.val == subRoot.val:
            if self.checkEqual(root, subRoot):
                return True
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)
        print(root.val, subRoot.val, left , right)
        if left or right:
            return True
    
        return False