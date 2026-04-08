class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # dfs
        m = len(grid)
        n = len(grid[0])
        
        def dfs(x, y):
            if grid[x][y] == '0' or grid[x][y] == '#':
                return 0
            
            grid[x][y] = '#'
            land = 1
            for dir_x, dir_y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = dir_x + x, dir_y + y
                if 0 <= nx < m and 0 <= ny < n:
                    land += dfs(nx, ny)
            return land

        res = 0
        for i in range(m):
            for j in range(n):
                if dfs(i, j):
                    res += 1
        return res