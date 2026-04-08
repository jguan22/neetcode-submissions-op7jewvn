class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(dict)
        for i, (a, b) in enumerate(equations):
            adj[a][b] = values[i]
            adj[b][a] = 1.0 / values[i]
            adj[a][a] = 1.0
            adj[b][b] = 1.0
        
        for start in adj.keys():
            queue = deque(adj[start].items())
            visited = {start}
            while queue:
                curr, res1 = queue.popleft()
                if curr in visited:
                    continue
                
                visited.add(curr)
                adj[start][curr] = res1

                for nxt, res2 in adj[curr].items():
                    if nxt not in visited:
                        newres = res1 * res2
                        queue.append((nxt, newres))
        

        ans = []
        for c, d in queries:
            if c in adj and d in adj[c]:
                ans.append(adj[c][d])
            else:
                ans.append(-1.0)

        return ans