# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        base = [root]

        def solve(node, value):
            if node.val == value:
                if node.left:
                    base.append(node.left)
                if node.right:
                    base.append(node.right)
                return True
            else:
                if node.left:
                    if node.left.val == value:
                        solve(node.left, value)
                        node.left = None
                    else:
                       solve(node.left, value) 
                if node.right:
                    if node.right.val == value:
                        solve(node.right, value)
                        node.right = None
                    else:
                        solve(node.right, value)
                return False
        # to_remove = []
        for d in to_delete:
            for tree in base:
                if tree.val == d:
                    if tree.left:
                        base.append(tree.left)
                    if tree.right:
                        base.append(tree.right)
                    base.remove(tree)
                    break
                if solve(tree, d):
                    break
        # for r in to_remove:
        #     base.remove(r)
        return base
        