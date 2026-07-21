class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # starting with rotten fruit: O(m*n)
        m = len(grid)
        n = len(grid[0])
        queue = deque()
        total_fruit = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                    total_fruit += 1

                if grid[i][j] == 1:
                    total_fruit += 1
        
        # bfs: O(m*n)
        minute = 0
        count = 0
        while queue:
            x, y, minute = queue.popleft()
            count += 1
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    grid[nx][ny] = 2
                    queue.append((nx, ny, minute + 1))
        
        return minute if count == total_fruit else -1