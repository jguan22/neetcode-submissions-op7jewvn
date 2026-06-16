class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build the graph
        adj_list = defaultdict(list)
        indegree = [0] * numCourses
        for a, b in prerequisites:
            adj_list[a].append(b)
            indegree[b] += 1
        
        # start exploring from source nodes
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        count = 0
        while queue:
            a = queue.popleft()
            count += 1

            for b in adj_list[a]:
                indegree[b] -= 1
                if indegree[b] == 0:
                    queue.append(b)
        
        return count == numCourses
