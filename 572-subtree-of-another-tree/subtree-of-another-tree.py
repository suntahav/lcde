# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node):
        res = ''
        if node is None:
            return '|N|'
        else:
            res += '|' + str(node.val) + '|'
            left = self.dfs(node.left)
            right = self.dfs(node.right)
            res += left
            res += right
        return res
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #Do DFS and make strings and see if the subtree string is in main tree
        main_tree = self.dfs(root)
        subtree = self.dfs(subRoot)
        if subtree in main_tree :
            return True
        else:
            return False