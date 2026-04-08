class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n:
                return 0

            if grid[x][y] == -1 or grid[x][y] == 0:
                return 0
            
            grid[x][y] = -1
            area = 1
            area += dfs(x+1, y)
            area += dfs(x-1, y)
            area += dfs(x, y+1)
            area += dfs(x, y-1)
            return area
        
        maxArea = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, dfs(i, j))
        return maxArea