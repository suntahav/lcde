# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraverse(self, root, arr):
        if root:
            self.inorderTraverse(root.left, arr)
            arr.append(root.val)
            self.inorderTraverse(root.right, arr)
        return
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        self.inorderTraverse(root, arr)
        return arr[k-1]