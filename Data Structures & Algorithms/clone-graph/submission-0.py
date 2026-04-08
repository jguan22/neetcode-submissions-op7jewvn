"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        root = Node(node.val)
        # track on current node list
        checked = set()
        built = {node.val:root}


        def DFS(curr, copy):
            # base case: node was checked
            if curr in checked:
                return
            
            checked.add(curr)
            for neighbor in curr.neighbors:
                if neighbor.val not in built:
                    new_neigh = Node(neighbor.val)
                    built[neighbor.val] = new_neigh
                else:
                    new_neigh = built[neighbor.val]
                
                copy.neighbors.append(new_neigh)
                DFS(neighbor, new_neigh)
    

        DFS(node, root)
        return root