class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # valid tree has n-1 edges and no circle
        if len(edges) != n-1:
            return False
        
        if n == 1:
            return True
        
        indegree = [0] * n
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            indegree[a] += 1
            indegree[b] += 1

        # trim the leaves
        queue = deque()
        for i in range(n):
            if indegree[i] == 1:
                queue.append(i)
        
        visited = 0
        while queue:
            i = queue.popleft()
            visited += 1
            indegree[i] -= 1 

            for j in adj[i]:
                indegree[j] -= 1
                if indegree[j] == 1:
                    queue.append(j)
        
        return visited == n