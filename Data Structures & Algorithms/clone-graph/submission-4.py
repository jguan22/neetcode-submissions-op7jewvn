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

        # use a dict to map original nodes to copy ones
        node_map = {}

        # dfs explore all nodes and edges: O(E + V)
        def dfs(curr):
            # base case:
            if curr in node_map:
                return node_map[curr]
            
            # copy the node and explore from it
            copy = Node(curr.val)
            node_map[curr] = copy
            for nxt in curr.neighbors:
                copy.neighbors.append(dfs(nxt))

            return copy
        
        return dfs(node)
