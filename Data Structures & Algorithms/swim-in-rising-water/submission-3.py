class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # modified Dijkstra: looking for the path with least max value
        n = len(grid)
        min_heap = [(grid[0][0], 0, 0)]   # (cost, x, y)
        visited = set((0, 0))
        
        while min_heap:
            curr_time, x, y = heapq.heappop(min_heap)

            if x == n-1 and y == n-1:
                return curr_time
            
            for dir_x, dir_y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = dir_x + x, dir_y + y
                if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    nxt_time = max(grid[nx][ny], curr_time)
                    heapq.heappush(min_heap, (nxt_time, nx, ny))
        
        return -1