# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def calculate(node):
            if node == None:
                return True, 0
            
            left = calculate(node.left)
            if not left[0]:
                return False, 0
            right = calculate(node.right)

            if left[0] and right[0]:
                if abs(left[1] - right[1]) <=1 :
                    return True, max(left[1], right[1]) + 1
            return False, 0
    
        return calculate(root)[0]
        