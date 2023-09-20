"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        new_nodes = {}
        visited = {}
        root = None
        def createCopy(n):
            if n:
                if n.val not in new_nodes:
                    new_node = Node(n.val)
                    new_nodes[n.val] = new_node
                    if n.neighbors:
                        neighbours = []
                        for nbr in n.neighbors:
                            if nbr:
                                neighbours.append(createCopy(nbr))
                        new_node.neighbors = neighbours
                    return new_node
                else:
                    #This border case when the new node has already been created and being reused for neighbors
                    return new_nodes[n.val]
            return None
                        
        if node:
            root = createCopy(node)

            
        return root