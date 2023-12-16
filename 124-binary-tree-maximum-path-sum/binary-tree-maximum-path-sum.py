# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [-300000000]
        def solve(root):
            if not root:
                return 0
            left = solve(root.left)
            right = solve(root.right)

            temp = max(max(left, right)+root.val, root.val)
            ans = max(temp, left+right+root.val)
            res[0] = max(res[0], ans)
            return temp
        solve(root)
        return res[0]