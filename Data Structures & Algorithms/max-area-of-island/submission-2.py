class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # dfs from the each cell
        m = len(grid)
        n = len(grid[0])

        def dfs(x, y):
            # base case
            if not (0 <= x < m and 0 <= y < n and grid[x][y] == 1):
                return 0

            # mark cell as visited:
            grid[x][y] = 2

            # explore all directions
            count = 1
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = dx + x, dy + y
                count += dfs(nx, ny)

            return count

        # explore the grid: O(m*n)
        max_area = 0
        for i in range(m):
            for j in range(n):
                max_area = max(dfs(i, j), max_area)

        return max_area