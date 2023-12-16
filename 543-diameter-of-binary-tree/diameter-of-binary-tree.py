# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [-1000]
        def calculate(node):
            # returns (max_diameter_till_now_including_this_node, max_length_of_subtree_including_this_node)
            if node == None:
                return 0
            left = calculate(node.left)
            right = calculate(node.right)
            if res[0] < left+right+1:
                res[0] = left+right+1
            return max(left, right)+1
        calculate(root)
        return res[0]-1