# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = []
        def calculate(node, prev_max):
            if node==None:
                return
            if node.val >= prev_max:
                res.append(node.val)
            calculate(node.left, max(prev_max, node.val))
            calculate(node.right, max(prev_max, node.val))
            return 
        calculate(root, -10000000)
        return len(res)
        