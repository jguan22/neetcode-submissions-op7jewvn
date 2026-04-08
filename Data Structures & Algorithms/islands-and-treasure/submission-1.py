class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # bfs
        m = len(grid)
        n = len(grid[0])
        queue = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append((i, j))
        
        while queue:
            l = len(queue)
            for _ in range(l):
                x, y = queue.popleft()

                for dir_x, dir_y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = dir_x+x, dir_y+y
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 2147483647:
                        grid[nx][ny] = grid[x][y] + 1
                        queue.append((nx, ny))