# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if preorder:
            if len(preorder) == 1:
                return TreeNode(preorder[0], None, None)
            else:
                # print(preorder)
                root = TreeNode(preorder[0], None, None)
                root_elem = preorder[0]

                inorder_idx = inorder.index(root_elem)

                left_inorder_subtree = inorder[: inorder_idx]
                if len(inorder) >= inorder_idx + 1:
                    right_inorder_subtree = inorder[inorder_idx + 1: ]
                else:
                    right_inorder_subtree = []
                
                if left_inorder_subtree:
                    left_preorder_subtree = preorder[1: 1+len(left_inorder_subtree)]
                    if right_inorder_subtree:
                        right_preorder_subtree = preorder[1+len(left_inorder_subtree) :]
                    else:
                        right_preorder_subtree = []
                else:
                    left_preorder_subtree = []
                    right_preorder_subtree = preorder[1:]
                
                root.left = self.buildTree(left_preorder_subtree, left_inorder_subtree)
                root.right = self.buildTree(right_preorder_subtree, right_inorder_subtree)
                return root
                
                


        else:
            return None
        

