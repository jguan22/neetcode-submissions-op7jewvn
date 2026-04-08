class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        # build two directed graphs based on the row and col condition
        # there shouldn't be any cycles in the graph, else no answer
        
        def findOrder(conditions):
            adj = defaultdict(list)
            indegree = [0] * (k+1)
            for u, v in conditions:
                adj[u].append(v)
                indegree[v] += 1

            queue = deque([x for x in range(1, k + 1) if indegree[x] == 0])
            res = {}
            i = 0
            while queue:
                x = queue.popleft()
                # map x to its index in the list
                res[x] = i
                i += 1
                for y in adj[x]:
                    indegree[y] -= 1
                    if indegree[y] == 0:
                        queue.append(y)
            return res if i == k else None
        

        rowOrder = findOrder(rowConditions)
        colOrder = findOrder(colConditions)
        if not rowOrder or not colOrder:
            return []
        
        # build the matrix
        matrix = [[0] * k for _ in range(k)]
        for i in range(1, k+1):
            r, c = rowOrder[i], colOrder[i]
            matrix[r][c] = i
        return matrix