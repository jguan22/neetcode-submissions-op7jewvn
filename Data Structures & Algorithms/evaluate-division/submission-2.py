class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # build graph
        adj_list = defaultdict(dict)
        for i, (a, b) in enumerate(equations):
            adj_list[a][b] = values[i]
            adj_list[b][a] = 1.0 / values[i]
            adj_list[a][a] = 1.0
            adj_list[b][b] = 1.0
        
        # find all path starting from each node
        for a in adj_list.keys():
            queue = deque([a])
            visited = {a}
            while queue:
                curr = queue.popleft()
                division = adj_list[a][curr]
                for nxt in adj_list[curr]:
                    if nxt not in visited:
                        visited.add(nxt)
                        queue.append(nxt)

                        nxt_division = adj_list[curr][nxt]
                        adj_list[a][nxt] = division * nxt_division
        
        # prepare ans
        ans = []
        for a, b in queries:
            if a in adj_list and b in adj_list[a]:
                ans.append(adj_list[a][b])
            else:
                ans.append(-1.0)
        return ans