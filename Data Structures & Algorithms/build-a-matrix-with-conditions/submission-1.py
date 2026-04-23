class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        # build the graph for both rows and cols to find sequences
        def findSequence(conditions):
            adj_list = defaultdict(list)
            indegree = [0] * (k+1)
            for u, v in conditions:
                adj_list[u].append(v)
                indegree[v] += 1     

            queue = deque()
            for i in range(1, k+1):
                if indegree[i] == 0:
                    queue.append(i)
            
            seq = defaultdict(int)
            count = 0
            while queue:
                curr = queue.popleft()
                seq[curr] = count
                count += 1

                for nxt in adj_list[curr]:
                    indegree[nxt] -= 1
                    if indegree[nxt] == 0:
                        queue.append(nxt)
                
            return seq if count == k else None
        

        rowSeq = findSequence(rowConditions)
        colSeq = findSequence(colConditions)
        if not rowSeq or not colSeq:
            return []
        
        # build matrix
        matrix = [[0] * k for _ in range(k)]
        for i in range(1, k+1):
            matrix[rowSeq[i]][colSeq[i]] = i
        
        return matrix