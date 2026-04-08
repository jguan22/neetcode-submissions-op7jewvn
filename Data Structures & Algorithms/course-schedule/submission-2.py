class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # graph sorting: cycle detection
        # use in-degree
        in_degree = defaultdict(int)
        adj = defaultdict(list)
        for a, b in prerequisites:
            adj[b].append(a)
            in_degree[a] += 1

        queue = deque()
        complete = 0
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
                complete += 1
        
        while queue:
            i = queue.popleft()
            for j in adj[i]:
                in_degree[j] -= 1
                if in_degree[j] == 0:
                    queue.append(j)
                    complete += 1
        return complete == numCourses