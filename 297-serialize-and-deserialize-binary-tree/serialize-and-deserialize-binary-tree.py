# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def preorder(node, s=''):
            if node:
                s += '('
                s += str(node.val)
                s += preorder(node.left) 
                s +=  preorder(node.right) 
                s += ')'
            else:
                s = '()'
            return s

        return preorder(root)
            
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def createTree(s):
            # print(s)
            if len(s) > 0:
                root_val = ''
                i = 1
                while s[i] != '(':
                    if s[i] == ')':
                        break
                    root_val += s[i]
                    i += 1
                if i == 1:
                    return None
                # print(root_val)
                root_val = int(root_val.strip())
                root_node = TreeNode(root_val)
                #Handle left substring
                start_left = i
                counter_start = 1
                counter_close = 0
                while counter_start != counter_close:
                    i += 1
                    if s[i] == '(':
                        counter_start += 1
                    if s[i] == ')':
                        counter_close += 1
                    
                left_str = s[start_left : i+1 ]

                #Handle Right substring
                right_str = s[i+1:-1]
                # print("left ----- ", left_str)
                # print("right ------- ", right_str )
                root_node.left = createTree(left_str)
                root_node.right = createTree(right_str)
                return root_node
            else:
                return None
        # print(data)
        return createTree(data)
                


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))