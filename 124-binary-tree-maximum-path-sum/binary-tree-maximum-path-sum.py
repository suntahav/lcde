# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            # if node:
            #     left_max, optim_left, optim_tree_left = dfs(node.left)
            #     right_max, optim_right, optim_tree_right = dfs(node.right)
            #     optim_sub = max(optim_left, optim_right, 0) + node.val
            #     optim_tree = optim_left + optim_right + node.val
            #     max_val = max([left_max, right_max, optim_sub, node.val, optim_tree])
            #     return max_val, optim_sub, optim_tree
            # else:
            #     return -100000000, 0, 0

            if node: #if node exist
                #check left for its max tree and max left subtree (no split)
                left_tree, left_max = dfs(node.left)
                #do same for right
                right_tree, right_max = dfs(node.right)
                #take equal to 0 because if negative no sense in taking 
                left_max = max(left_max, 0)
                #same for right
                right_max = max(right_max, 0)
                #create the optimal tree for this tree as it is final answer
                cur_tree = node.val + left_max + right_max
                #create a subtree for level above
                cur_max = node.val + max(left_max, right_max)
                #calculate the best complete tree among all
                overall_best_tree = max(left_tree, right_tree, cur_tree)
                #return both the optimal tree and subtree to be used as branch
                return overall_best_tree, cur_max
            else:
                #return negative infinity as there can be negative tree as well and 0 for max val
                return float('-inf'), 0
                    
        tree, max_val = dfs(root)
        return max(tree, max_val)

        