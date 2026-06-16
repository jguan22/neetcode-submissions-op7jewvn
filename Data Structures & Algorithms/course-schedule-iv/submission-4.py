class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # build the graph: find a path from a to b
        adj_list = defaultdict(list)
        indegree = [0] * numCourses
        for a, b in prerequisites:
            adj_list[a].append(b)
            indegree[b] += 1
        
        # precompute all prerequeisites
        pre_set = defaultdict(set)
        queue = deque()

        # start exploring from source nodes
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        # bfs
        while queue:
            a = queue.popleft()
            for b in adj_list[a]:
                # all pre of source a should be pre of b as well
                pre_set[b].update(pre_set[a])
                pre_set[b].add(a)

                indegree[b] -= 1
                if indegree[b] == 0:
                    queue.append(b)
        
        # prepare ans to queries
        ans = [False] * len(queries)
        for i, (a, b) in enumerate(queries):
            if a in pre_set[b]:
                ans[i] = True
                
        return ans