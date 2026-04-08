class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # pre-compute all possible divisions
        adj = defaultdict(dict)
        for i, (a, b) in enumerate(equations):
            adj[a][b] = values[i]
            adj[b][a] = 1.0 / values[i]
            adj[a][a] = 1.0
            adj[b][b] = 1.0
        
        for a in adj.keys():
            queue = deque(adj[a].items())
            visited = {a}
            while queue:
                curr, res1 = queue.popleft()
                if curr in visited:
                    continue
                visited.add(curr)
                adj[a][curr] = res1

                for nxt, res2 in adj[curr].items():
                    if nxt not in visited:
                        newDivision = res1 * res2
                        queue.append((nxt, newDivision))
        
        ans = []
        for q in queries:
            if q[0] in adj:
                if q[1] in adj[q[0]]:
                    ans.append(adj[q[0]][q[1]])
                    continue
            ans.append(-1.0)
            
        return ans