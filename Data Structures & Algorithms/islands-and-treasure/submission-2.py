class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # bfs: starting from treasure to fill the grid
        queue = deque()
        m = len(grid)
        n = len(grid[0])
        inf = 2**31 - 1

        # find all treasues: O(m*n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append((i, j ,0))
        
        # explore the gird: O(m*n)
        while queue:
            x, y, dist = queue.popleft()
            
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == inf:
                    grid[nx][ny] = dist + 1
                    queue.append((nx, ny, dist + 1))
