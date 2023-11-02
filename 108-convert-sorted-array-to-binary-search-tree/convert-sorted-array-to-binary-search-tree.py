# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def create(arr):
            if len(arr) >= 1:
                mid = len(arr) // 2
                val = arr[mid]
                root = TreeNode(val)
                root.left = create(arr[:mid])
                root.right = create(arr[mid+1:])
                return root
            else:
                return None
        return create(nums)
        