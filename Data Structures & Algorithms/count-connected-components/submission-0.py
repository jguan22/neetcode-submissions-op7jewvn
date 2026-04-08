class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # build graph
        adj_list = defaultdict(list)
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
        
        visited = set()


        def dfs(node, pre):
            if node in visited:
                return
            
            visited.add(node)
            for neigh in adj_list[node]:
                if neigh == pre:
                    continue
                dfs(neigh, node)
            
        
        # run dfs on all nodes
        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i, -1)
                count += 1
        
        return count