# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #Queue approach
        res = []
        #make queue
        queue = collections.deque()
        queue.append(root)
        while queue:
            #calcualte the len at the time (all child members of level)
            qlen = len(queue)
            level = []
            for i in range(qlen):
                item = queue.popleft()
                if item: #if item in not null
                    level.append(item.val)
                    queue.append(item.left)
                    queue.append(item.right)
            
            if level: #check level empty
                res.append(level)
        return res
            