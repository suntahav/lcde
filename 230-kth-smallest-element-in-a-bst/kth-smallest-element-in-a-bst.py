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
                #add all left nodes starting from left
                arr.append(curr)
                curr = curr.left
            # if not arr:
            #     #no nodes in arr empty not possible
            #     break
            
            #pop the node
            elem = arr.pop()
            #reduce the count
            k -= 1

            if k==0:
                #if reached then the recently popped node is the node
                return elem.val
            #else move to right and repeat same process
            curr = elem.right
        