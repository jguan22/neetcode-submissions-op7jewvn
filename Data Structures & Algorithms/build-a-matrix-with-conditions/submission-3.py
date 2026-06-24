class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        # need to set orders for both row and col

        # helper to set Orders
        def setOrder(conditions):
            # build graph: O(E)
            adj_list = defaultdict(list)
            indegree = [0] * (k+1)
            for a, b in conditions:
                adj_list[a].append(b)
                indegree[b] += 1
            
            # starting from nodes with 0 indegree
            queue = deque([i for i in range(1, k+1) if indegree[i] == 0])

            # build order list: map num to index: O(E)
            orders = defaultdict(int)
            index = 0 
            while queue:
                num = queue.popleft()
                orders[num] = index
                index += 1

                for nxt in adj_list[num]:
                    indegree[nxt] -= 1
                    if indegree[nxt] == 0:
                        queue.append(nxt)
            
            return orders if index == k else None
        
        rowOrder = setOrder(rowConditions)
        colOrder = setOrder(colConditions)
        if not rowOrder or not colOrder:
            return []
        
        # build matrix: O(k^2)
        matrix = [[0] * k for _ in range(k)]
        for i in range(1, k+1):
            matrix[rowOrder[i]][colOrder[i]] = i
        
        return matrix