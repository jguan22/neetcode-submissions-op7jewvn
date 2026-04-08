class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(set)
        for a, b in prerequisites:
            adj[a].add(b)
        
        
        def find(x, y):
            visited = {x}
            queue = deque(adj[x])
            while queue:
                curr = queue.popleft()
                if curr in visited:
                    continue
                visited.add(curr)
                # add node to neighbor of start for later fast quries
                adj[x].add(curr)
                if curr == y:
                    return True

                for nei in adj[curr]:
                    queue.append(nei)
            return False
            
        res = []
        for u, v in queries:
            if v in adj[u]:
                res.append(True)
            else:
                res.append(find(u, v))
        return res