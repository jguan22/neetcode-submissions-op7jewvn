class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # instead of marking surrounded cells, mark not surrounded ones
        m = len(board)
        n = len(board[0])

        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n:
                return
            if board[x][y] == 'X' or board[x][y] == 'U':
                return

            board[x][y] = 'U'
            for dir_x, dir_y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = dir_x + x, dir_y + y
                dfs(nx, ny)

        
        # cells at the boarder is unsurrounded ones
        for i in range(m):
            dfs(i, 0)
            dfs(i, n-1)
        for i in range(n):
            dfs(0, i)
            dfs(m-1, i)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'U':
                    board[i][j] = 'O'