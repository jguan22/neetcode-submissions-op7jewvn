class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # build the directed graph as dict to store weight of edges
        adj_list = defaultdict(dict)
        for i, (a, b) in enumerate(equations):
            adj_list[a][b] = values[i]
            adj_list[b][a] = 1.0 / values[i]
            adj_list[a][a] = 1.0
            adj_list[b][b] = 1.0
        
        # precompute all answers
        for start in adj_list.keys():
            # start exploring from node (bfs)
            queue = deque([start])
            visited = {start}
            while queue:
                curr = queue.popleft()
                division1 = adj_list[start][curr]

                for nxt in adj_list[curr]:
                    # find a new node, add it to adj list of start node
                    if nxt not in visited:
                        division2 = adj_list[curr][nxt]
                        adj_list[start][nxt] = division1 * division2

                        visited.add(nxt)
                        queue.append(nxt)
        
        # prepare ans for queries
        ans = [-1.0] * len(queries)
        for i, (a, b) in enumerate(queries):
            if a in adj_list and b in adj_list[a]:
                ans[i] = adj_list[a][b]
        
        return ans