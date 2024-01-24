# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:

        mapper = {1:0,
        2:0,
        3:0,
        4:0,
        5:0,
        6:0,
        7:0,
        8:0,
        9:0
        }
        res = [0]

        def calculate(node):
            if node:
                mapper[node.val] += 1
                if node.left == None and node.right == None:
                    odd = 0
                    for k in mapper.keys():
                        if mapper[k] % 2 == 1:
                            odd += 1
                    if odd <= 1:
                        res[0] += 1
                calculate(node.left)
                calculate(node.right)
                mapper[node.val] -= 1
        calculate(root)
        return res[0]
            
        