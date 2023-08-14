# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bfs(self, arr, root, level=0):
        if root is None:
            return
        #add the number to the 2d array at specific level
        arr[level].append(root.val)
        #traverse left and right with increased level
        if root.left is not None:
            self.bfs(arr, root.left, level+1)
        if root.right is not None:
            self.bfs(arr, root.right, level+1)
        
         

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #2d array for storing the numbers for each level : max is 2000 as a skewed tree
        arr = [[] for x in range(2001)]
        self.bfs(arr, root, level=0)
        res = []
        for i in range(2001):
            if len(arr[i]) != 0:
                res.append(arr[i])
        return res
