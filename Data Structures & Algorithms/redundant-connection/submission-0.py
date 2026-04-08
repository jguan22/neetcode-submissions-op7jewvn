class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # run dfs to find the cycle
        # build the graph
        visited = set()
        adj_list = defaultdict(list)
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
        
        start = -1
        cycle_set = set()
        def dfs(node, parent):
            nonlocal start
            # mark the first node in visited as start
            if node in visited:
                start = node
                return True
            
            visited.add(node)

            for neigh in adj_list[node]:
                if neigh == parent:
                    continue

                # mark the nodes in cycle until recurse back to start
                if dfs(neigh, node):
                    if start != -1:
                        cycle_set.add(neigh)
                
                    if node == start:
                        start = -1
                    return True
            return False
        
        dfs(1, -1)

        # loop through edges list
        n = len(edges)
        for i in range(n-1, -1, -1):
            edge = edges[i]
            if edge[0] in cycle_set and edge[1] in cycle_set:
                return edge
        
        return []