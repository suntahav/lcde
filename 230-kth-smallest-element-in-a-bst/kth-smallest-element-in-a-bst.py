# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = deque()
        curr = root
        while True:
            while curr:
                arr.append(curr)
                curr = curr.left
            if not arr:
                break
            
            elem = arr.pop()
            k -= 1

            if k==0:
                return elem.val
            
            curr = elem.right
        