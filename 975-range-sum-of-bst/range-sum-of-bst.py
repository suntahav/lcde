# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        def dfs(node):
            if node:
                res = 0
                if node.val >= low and node.val <= high:
                    res += node.val
                res += dfs(node.left)
                res += dfs(node.right)
                return res
            else:
                return 0
        return dfs(root)
        