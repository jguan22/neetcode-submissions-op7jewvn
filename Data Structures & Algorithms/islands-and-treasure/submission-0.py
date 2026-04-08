class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])
        queue = deque()

        # starting from the gate
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 0:
                    queue.append((row, col))
        
        # do BFS on each gate
        directions = [
            (-1, 0), 
            (1, 0), 
            (0, -1), 
            (0, 1)
            ]

        distance = 0
        while queue:
            x, y = queue.popleft()

            for dir_x, dir_y in directions:
                x_next, y_next = dir_x + x, dir_y + y

                if 0 <= x_next < m and 0 <= y_next < n and grid[x_next][y_next] == 2147483647:
                    grid[x_next][y_next] = grid[x][y] + 1
                    queue.append((x_next, y_next))
                
                
        return