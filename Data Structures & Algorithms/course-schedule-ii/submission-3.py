class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # convert to a graph problem: return a valid topical order of graph
        # build the graph
        adj_list = defaultdict(list)
        indegree = [0] * numCourses
        for a, b in prerequisites:
            adj_list[b].append(a)
            indegree[a] += 1
        
        # explore from node with 0 indegree
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        # run bfs: O(V+E)
        order = []
        count = 0
        while queue:
            curr = queue.popleft()
            order.append(curr)
            count += 1

            for nxt in adj_list[curr]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)
        
        return order if count == numCourses else []