class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # find all rotten ones
        m = len(grid)
        n = len(grid[0])
        queue = deque()
        good_ones = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    good_ones += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))
        
        minutes = 0
        while queue and good_ones > 0:
            minutes += 1
            l = len(queue)
            for _ in range(l):
                x, y = queue.popleft()
                for dir_x, dir_y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = dir_x + x, dir_y + y
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        good_ones -= 1
                        queue.append((nx, ny))
        
        return minutes if good_ones == 0 else -1