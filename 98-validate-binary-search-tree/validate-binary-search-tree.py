# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _isValidBST(self, root, mx=None, mn=None):
        if root is None:
            return True
        if root.val < mx and root.val > mn:
            left = self._isValidBST(root.left, mn = mn, mx = min(root.val, mx))
            right = self._isValidBST(root.right, mn = max(mn, root.val), mx = mx)
            if left and right:
                return True
        return False
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self._isValidBST(root, mx = float("inf"), mn = float('-inf'))
        
        
        
        
        
