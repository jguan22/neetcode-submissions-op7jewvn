class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # find all rotten ones
        m = len(grid)
        n = len(grid[0])
        queue = deque()
        good_ones = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] == 1:
                    good_ones += 1

        # bfs from rotten ones
        directions = [
            (-1, 0), 
            (1, 0), 
            (0, -1), 
            (0, 1)
            ]
            
        minute = -1
        count = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                x, y = queue.popleft()
                for dir_x, dir_y in directions:
                    nx, ny = x + dir_x, y + dir_y
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        queue.append((nx, ny))
                        count += 1
            minute += 1
        
        return max(0, minute) if good_ones == count else -1