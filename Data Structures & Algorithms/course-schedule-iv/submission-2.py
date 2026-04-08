class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(set)
        for a, b in prerequisites:
            adj[a].add(b)
        
        # build the prerequisite map
        for i in range(numCourses):
            queue = deque([i])
            visited = {i}
            while queue:
                curr = queue.popleft()
                # i is the prerequisite for all reachable nodes
                if curr != i:
                    adj[i].add(curr)

                for nei in adj[curr]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append(nei)
            
        res = [None] * len(queries)
        for i, (u, v) in enumerate(queries):
            res[i] = True if v in adj[u] else False
        return res