# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        res = {'count':0}
        def calc(root):
            if root.left == None and root.right == None:
                res['count'] += 1
                return root.val, 1
            elif root.left == None:
                temp, nodes = calc(root.right)
                if root.val == (temp + root.val) //(nodes+1):
                    res['count'] += 1
                return temp + root.val, nodes +1
            elif root.right == None:
                temp, nodes = calc(root.left)
                if root.val == (temp + root.val)// (nodes+1):
                    print(root.val)
                    res['count'] += 1
                return root.val + temp, nodes+1
            else:
                left, n_left = calc(root.left)
                right, n_right = calc(root.right)
                if root.val == (left + right + root.val)//(n_left + n_right+ 1):
                    res['count'] += 1
                return root.val + left + right, n_left + n_right+ 1
                
        _,_= calc(root)
        return res['count']

        