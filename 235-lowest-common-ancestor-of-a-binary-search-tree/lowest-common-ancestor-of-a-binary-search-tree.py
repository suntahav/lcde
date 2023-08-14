# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # multiplication is positive if both on same side of node and 0 when either one is equal (case of answer)
        checkval = (root.val - p.val) * (root.val - q.val)
        if checkval <= 0:
            return root
        else:
            #otherwise check the subtrees
            if root.val > p.val:
                return self.lowestCommonAncestor(root.left, p, q)
            else:
                return self.lowestCommonAncestor(root.right, p, q)