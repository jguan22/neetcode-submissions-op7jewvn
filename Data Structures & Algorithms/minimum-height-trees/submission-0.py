class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # use indegree
        if n == 1:
            return [0]

        adj = defaultdict(list)
        indegree = [0] * n
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            indegree[a] += 1
            indegree[b] += 1
        
        # trim the leaf
        queue = deque()
        for i in range(n):
            if indegree[i] == 1:
                queue.append(i)
        
        while queue:
            n = len(queue)
            level = []
            for _ in range(n):
                leaf = queue.popleft()
                level.append(leaf)
                for nei in adj[leaf]:
                    indegree[nei] -= 1
                    if indegree[nei] == 1:
                        queue.append(nei)
        
        return level