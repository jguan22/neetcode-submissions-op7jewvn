class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        m = len(board)
        n = len(board[0])

        def dfs(x, y):
            board[x][y] = 'N'

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 'O':
                    dfs(nx, ny)

        # expand from edges to find non-surrounded regions
        for i in range(m):
            for j in range(n):
                if i == 0 or i == (m-1) or j == 0 or j == (n-1):
                    if board[i][j] == 'O':
                        dfs(i, j)

        # turn all remaining O to X, and N to O
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'N':
                    board[i][j] = 'O'
        return