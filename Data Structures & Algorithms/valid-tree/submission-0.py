class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # valid tree is a connected graph without any cycle
        # edge case:
        if len(edges) != n - 1:
            return False
            
        # build the graph
        adj_list = defaultdict(list)
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
        
        visited = set()
        

        def dfs(node, parent):
            if node in visited:
                return False
            
            visited.add(node)
            for neigh in adj_list[node]:
                # skip the node path from
                if neigh == parent:
                    continue
                if not dfs(neigh, node):
                    return False
            return True
        
        # run dfs: any node should have path to all nodes in the tree
        if not dfs(0, -1):
            return False
        return len(visited) == n