class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # dijkstra with total N^2 cells
        n = len(grid)
        min_heap = [(grid[0][0], 0, 0)]     # (cost, x, y)
        min_time = grid[0][0]
        visited = [[False] * n for _ in range(n)]
        
        # O(N^2logN^2) = O(N^2 logN)
        while min_heap:
            curr_time, x, y = heapq.heappop(min_heap)
            if visited[x][y]:
                continue
            visited[x][y] = True

            min_time = max(min_time, grid[x][y])

            if x == (n - 1) and y == (n - 1):
                return min_time
            
            for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    heapq.heappush(min_heap, (grid[nx][ny], nx, ny))
        
        return -1