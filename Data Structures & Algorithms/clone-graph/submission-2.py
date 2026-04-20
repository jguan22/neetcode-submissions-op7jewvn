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

        # map original node to the copied node
        node_map = {}

        def dfs(curr):
            if curr in node_map:
                return node_map[curr]
            
            curr_copy = Node(curr.val)
            node_map[curr] = curr_copy

            for nxt in curr.neighbors:
                curr_copy.neighbors.append(dfs(nxt))

            return curr_copy
    
        return dfs(node)