# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _isValidBST(self, root, mx=None, mn=None):
        #Define the left and right limit of each node and check recursively
        if root is None:
            #root doesnt exist means true
            return True
        if root.val < mx and root.val > mn: # in range
            #for left the min remains same but max is minimum or root node and original max
            left = self._isValidBST(root.left, mn = mn, mx = min(root.val, mx))
            #for right the max remains same but minimum must be greater than the max of root and the original minimum
            right = self._isValidBST(root.right, mn = max(mn, root.val), mx = mx)
            if left and right:
                return True
        return False
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self._isValidBST(root, mx = float("inf"), mn = float('-inf'))
        
        
        
        
        
