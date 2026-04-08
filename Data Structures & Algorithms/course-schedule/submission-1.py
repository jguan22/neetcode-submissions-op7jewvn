class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # using indegree
        indegree = [0] * numCourses
        adj_list = defaultdict(list)

        # build the graph
        for course, pre in prerequisites:
            adj_list[pre].append(course)
            indegree[course] += 1
        
        # find node with 0 indegree(sources)
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        # starting from sources
        count = 0
        while queue:
            node = queue.popleft()
            count += 1

            # decrement the indegree for all child nodes
            for neighbor in adj_list[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
            
        # check how many courses taken once all done
        return count == numCourses