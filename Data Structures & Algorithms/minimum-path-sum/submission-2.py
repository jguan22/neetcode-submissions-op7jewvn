class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # since it can only move down or right, the sum depends on its up and left cells
        m, n = len(grid), len(grid[0])

        # base case
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
        for j in range(1, n):
            grid[0][j] += grid[0][j-1]

        for i in range(1, m):
            for j in range(1, n):
                # pick the smaller sum from up and left
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        
        return grid[m-1][n-1]


        '''
        # dijkstra: O(mnlog(mn))
        min_heap = [(grid[0][0], 0, 0)]   # (curr_sum, x, y)
        m, n = len(grid), len(grid[0])
        visited = set()

        while min_heap:
            curr_sum, x, y = heapq.heappop(min_heap)

            if x == m - 1 and y == n - 1:
                return curr_sum

            if (x, y) in visited:
                continue
            visited.add((x, y))

            for dir_x, dir_y in [(1, 0), (0, 1)]:
                nx, ny = dir_x + x, dir_y + y
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                    heapq.heappush(min_heap, (curr_sum + grid[nx][ny], nx, ny))
        
        return -1
        '''