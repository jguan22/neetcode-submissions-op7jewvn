class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = defaultdict(list)
        for a, b in prerequisites:
            indegree[a] += 1
            adj[b].append(a)

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        complete = 0
        res = []
        while queue:
            i = queue.popleft()
            complete += 1
            res.append(i)

            for j in adj[i]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    queue.append(j)
        
        return res if complete == numCourses else []