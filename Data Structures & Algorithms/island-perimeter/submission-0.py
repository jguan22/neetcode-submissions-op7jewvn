class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        perimeter = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for dir_x, dir_y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nx, ny = dir_x + i, dir_y + j
                        if 0 <= nx < m and 0 <= ny < n:
                            if grid[nx][ny] == 0:
                                perimeter += 1
                        else:
                            perimeter += 1
        
        return perimeter