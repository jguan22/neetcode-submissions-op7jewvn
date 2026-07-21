class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # convert to a graph problem: detect if there is cycle in a directed graph
        # build the graph: O(V + E)
        adj_list = defaultdict(list)
        indegree = [0] * numCourses
        for u, v in prerequisites:
            adj_list[u].append(v)
            indegree[v] += 1
        
        # use bfs: starting from node with 0 indegree: O(V)
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        # bfs: O(V + E)
        count = 0
        while queue:
            curr = queue.popleft()
            count += 1

            for nxt in adj_list[curr]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)
        
        return count == numCourses