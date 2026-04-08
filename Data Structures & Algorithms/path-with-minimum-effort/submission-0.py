class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # Dijkstra
        m = len(heights)
        n = len(heights[0])
        heap = [(0, 0, 0)]  # (max effort, x, y)
        dp = [[float('inf')] * n for _ in range(m)]
        dp[0][0]

        while heap:
            curr_max, x, y = heapq.heappop(heap)
            # find the target
            if x == m - 1 and y == n - 1:
                return curr_max
            # find a better path previously
            if curr_max >= dp[x][y]:
                continue
            dp[x][y] = curr_max

            for dir_x, dir_y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = x + dir_x, y + dir_y
                if 0 <= nx < m and 0 <= ny < n:
                    nxt_max = max(curr_max, abs(heights[x][y] - heights[nx][ny]))
                    heapq.heappush(heap, (nxt_max, nx, ny))
        
        return dp[m-1][n-1]
