class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # find all 'O' connected to the borders
        m = len(board)
        n = len(board[0])
        queue = deque()
        
        for i in range(m):
            queue.append((i, 0))
            queue.append((i, n-1))
        for j in range(n):
            queue.append((0, j))
            queue.append((m-1, j))
        
        while queue:
            x, y = queue.popleft()
            if board[x][y] != 'O':
                continue
            
            # mark these 'O' to '#'
            board[x][y] = '#'

            for dir_x, dir_y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = dir_x + x, dir_y + y
                if 0 <= nx < m and 0 <= ny < n:
                    queue.append((nx, ny))
        
        # mark all surrounded cells and turn border ones back to 'O'
        for i in range(m):
            for j in range(n):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
        return