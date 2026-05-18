class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        # build two graphs for rows and cols to find sequence
        def findSequence(conditions):
            adj_list = defaultdict(list)
            indegree = [0] * (k+1)
            for a, b in conditions:
                adj_list[a].append(b)
                indegree[b] += 1
            
            queue = deque([num for num in range(1, k+1) if indegree[num] == 0])
            index = 0
            sequence = defaultdict(int)
            while queue:
                curr = queue.popleft()
                sequence[curr] = index
                index += 1

                for nxt in adj_list[curr]:
                    indegree[nxt] -= 1
                    if indegree[nxt] == 0:
                        queue.append(nxt)

            return sequence if index == k else None
        

        rowSeq = findSequence(rowConditions)
        colSeq = findSequence(colConditions)

        if not rowSeq or not colSeq:
            return []

        matrix = [[0] * k for _ in range(k)]
        for i in range(1, k+1):
            matrix[rowSeq[i]][colSeq[i]] = i
        return matrix