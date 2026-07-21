class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # traverse the flow backwards from both prcific and atlantic
        # ans is the intesection of both set
        m = len(heights)
        n = len(heights[0])
        pacific_shores = deque()
        atlantic_shores = deque()

        # starting from the shores: O(m*n)
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    pacific_shores.append((i, j))
                if i == m - 1 or j == n - 1:
                    atlantic_shores.append((i, j))
        
        # helper to run bfs: O(m*n)
        def bfs(q):
            res_set = set()
            while q:
                x, y = q.popleft()
                if (x, y) in res_set:
                    continue
                res_set.add((x, y))

                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and heights[nx][ny] >= heights[x][y]:
                        q.append((nx, ny))
            return res_set
        
        pacific_set = bfs(pacific_shores)
        atlantic_set = bfs(atlantic_shores)

        # the intersection of both sets are the answer: O(m*n)
        return list(pacific_set & atlantic_set)

