class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # find the min of max level in the route to destination
        n = len(grid)
        dp = [[float('inf')] * n for _ in range(n)]
        heap = [(grid[0][0], 0, 0)]   # (cost, x, y)

        while heap:
            curr_cost, x, y = heapq.heappop(heap)
            if x == n-1 and y == n-1:
                return curr_cost

            if curr_cost >= dp[x][y]:
                continue
            
            dp[x][y] = curr_cost
            for dir_x, dir_y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = dir_x + x, dir_y + y
                if 0 <= nx < n and 0 <= ny < n:
                    nxt_cost = max(curr_cost, grid[nx][ny])
                    heapq.heappush(heap, (nxt_cost, nx, ny))
        
        return -1