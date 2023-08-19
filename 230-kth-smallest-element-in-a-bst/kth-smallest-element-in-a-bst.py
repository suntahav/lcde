# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraverse(self, root, arr,k):
        if len(arr) == k:
            return
        if root:
            self.inorderTraverse(root.left, arr, k)
            if len(arr) == k:
                return
            arr.append(root.val)
            if len(arr) == k:
                return
            self.inorderTraverse(root.right, arr, k)
            if len(arr) == k:
                return
        return
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = deque()
        self.inorderTraverse(root, arr,k)
        return arr.pop()