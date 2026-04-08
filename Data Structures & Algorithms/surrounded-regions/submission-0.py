class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # starting from the edge cells, the rest are surrounded regions
        m = len(board)
        n = len(board[0])
        queue = deque()
        for i in range(m):
            queue.append((i, 0))
            queue.append((i, n-1))
            
        
        for j in range(n):
            queue.append((0, j))
            queue.append((m-1, j))
        
        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]
        visited = [[False] * n for _ in range(m)]
        while queue:
            x, y = queue.popleft()
            visited[x][y] = True

            if board[x][y] == 'X':
                continue

            if board[x][y] == 'O':
                board[x][y] = 'Y'
            
            for dir_x, dir_y in directions:
                nx, ny = x + dir_x, y + dir_y
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    queue.append((nx, ny))
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'Y':
                    board[i][j] = 'O'
        
        return