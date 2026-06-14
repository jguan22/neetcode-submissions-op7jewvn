"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # sanity check
        if not node:
            return None

        # use a dict to map original node to copy node
        node_map = {}
        queue = deque([node])
        node_map[node] = Node(node.val)

        while queue:
            curr = queue.popleft()
            
            # explore all neighbors
            for nxt in curr.neighbors:
                # create node if not copied yet
                if nxt not in node_map:
                    node_map[nxt] = Node(nxt.val)
                    queue.append(nxt)
                
                # add it to neighbor list
                node_map[curr].neighbors.append(node_map[nxt])
        
        return node_map[node]