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
    def checkIncreasing(self, arr):
        length = len(arr)
        flag = True
        if len(arr) == 1:
            return flag
        for i in range(1, len(arr)):
            if arr[i] <= arr[i-1]:
                flag = False
                break
        return flag

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = []
        self.inorderTraverse(root, arr)
        if arr:
            return self.checkIncreasing(arr)
        else:
            return True

        
        
        
        
        
