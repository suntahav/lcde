# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def calculate(node):
            # returns (max_diameter_till_now_including_this_node, max_length_of_subtree_including_this_node)
            if node==None:
                return (0,0)
            if node.right==None:
                a = calculate(node.left)
                return (max(a[0], a[1]+1), a[1]+1)
            if node.left==None:
                a = calculate(node.right)
                return (max(a[0], a[1]+1), a[1]+1)
            
            left = calculate(node.left)
            right = calculate(node.right)
            max_dia_this_node = left[1]+1+right[1]
            max_dim = max(max_dia_this_node, max(left[0], right[0]))
            max_sub = 1 + max(left[1], right[1])
            return (max_dim, max_sub)
        return calculate(root)[0]-1