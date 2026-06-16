class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build the graph
        adj_list = defaultdict(list)
        indegree = [0] * numCourses
        for a, b in prerequisites:
            adj_list[b].append(a)
            indegree[a] += 1

        # start exploring from source nodes
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        ans = []
        count = 0
        while queue:
            # take course and increment counts
            a = queue.popleft()
            ans.append(a)
            count += 1

            # release prerequisite of adjcent courses
            for b in adj_list[a]:
                indegree[b] -= 1
                if indegree[b] == 0:
                    queue.append(b)
        
        return ans if count == numCourses else []