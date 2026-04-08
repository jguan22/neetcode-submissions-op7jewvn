class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # find shortest weighted path
        # modified Dijkstra (dist, x, y)
        m = len(grid)
        n = len(grid[0])
        min_heap = [(grid[0][0], 0, 0)]
        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        visited = set()
        while min_heap:
            dist, x, y = heapq.heappop(min_heap)

            if (x, y) in visited:
                continue
            visited.add((x, y))

            # base case: find target (m-1, n-1)
            if x == m-1 and y == n-1:
                return dist
            
            for dir_x, dir_y in directions:
                nx, ny = dir_x + x, dir_y + y
                if 0 <= nx < m and 0 <= ny < n:
                    new_dist = grid[nx][ny] if grid[nx][ny] > dist else dist
                    heapq.heappush(min_heap, (new_dist, nx, ny))
        
        return -1