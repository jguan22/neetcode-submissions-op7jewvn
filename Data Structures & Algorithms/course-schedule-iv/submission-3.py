class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # graph: find a path from a to b
        adj_list = defaultdict(list)
        indegree = [0] * numCourses
        for a, b in prerequisites:
            adj_list[a].append(b)
            indegree[b] += 1
    
        # precompute all path: start from roots
        pre_set = [set() for _ in range(numCourses)]
        queue = deque([node for node in range(numCourses) if indegree[node] == 0])

        while queue:
            a = queue.popleft()

            for b in adj_list[a]:
                # add a and all pre of a to b
                pre_set[b].add(a)
                pre_set[b].update(pre_set[a])

                # explore b when it becomes a root
                indegree[b] -= 1
                if indegree[b] == 0:
                    queue.append(b)
                
        # query
        ans = [False] * len(queries)
        for i, (a, b) in enumerate(queries):
            if a in pre_set[b]:
                ans[i] = True
        return ans