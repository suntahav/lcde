# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = {}
        def dfs(node, level):
            if node:
                if level not in res:
                    res[level] = node.val
                    dfs(node.right, level+1)
                    dfs(node.left, level+1)
                else:
                    dfs(node.right, level+1)
                    dfs(node.left, level+1)
            else:
                return
        dfs(root, 0)
        keys = sorted(list(res.keys()))
        return [res[k] for k in keys]

                
        