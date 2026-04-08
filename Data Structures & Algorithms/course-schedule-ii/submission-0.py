class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # use indegree
        indegree = [0] * numCourses
        adj_list = defaultdict(list)
        for course, pre in prerequisites:
            adj_list[pre].append(course)
            indegree[course] += 1
        
        # find all source nodes
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
            
        ans = []
        while queue:
            node = queue.popleft()
            ans.append(node)

            for child in adj_list[node]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)
        
        return ans if len(ans) == numCourses else []