# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if node:
                left_max, optim_left, optim_tree_left = dfs(node.left)
                right_max, optim_right, optim_tree_right = dfs(node.right)
                optim_sub = max(optim_left, optim_right, 0) + node.val
                optim_tree = optim_left + optim_right + node.val
                max_val = max([left_max, right_max, optim_sub, node.val, optim_tree])
                return max_val, optim_sub, optim_tree
            else:
                return -100000000, 0, 0
                    
        max_val, sub, tree = dfs(root)
        return max(max(tree, max_val), sub)

        