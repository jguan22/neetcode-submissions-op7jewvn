class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(set)
        for a, b in prerequisites:
            adj[a].add(b)
        
        # build the prerequisite map
        for i in range(numCourses):
            queue = deque(adj[i])
            visited = {i}
            while queue:
                curr = queue.popleft()
                if curr in visited:
                    continue
                visited.add(curr)

                # i is the prerequisite for all reachable nodes
                adj[i].add(curr)
                for nei in adj[curr]:
                    queue.append(nei)
            
        res = [None] * len(queries)
        for i, (u, v) in enumerate(queries):
            res[i] = True if v in adj[u] else False
        return res