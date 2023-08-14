# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEqual(self, root, subRoot):
        #First 3 ifs check the edge cases because we need to match exact subtree including Nulls
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
               #only if equal subtree we say yes
                return True
         # If the root value matches but not equal we still have to check left and right for subtrees
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)
        if left or right:
            #either one satisfies will work
            return True
    
        return False