class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # dfs from the each cell
        m = len(grid)
        n = len(grid[0])

        def dfs(x, y):
            # mark cell as visited:
            grid[x][y] = '2'

            # explore all directions
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = dx + x, dy + y
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1':
                    dfs(nx, ny)

        # explore the grid: O(m*n)
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count