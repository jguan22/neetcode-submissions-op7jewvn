class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        l = len(word) - 1
        m = len(board)
        n = len(board[0])

        # a matrix to track if cell is visited
        visited = [[0] * n for _ in range(m)]

        # need an index to track which position of board
        # an index to track the letter to match
        def backtrack(x, y, i):
            # base case
            if i > l:
                return True
            
            # out of board
            if x >= m or x < 0 or y >= n or y < 0:
                return False

            if visited[x][y] or board[x][y] != word[i]:
                return False
        
            # if current letter match, keep search its neighbours
            visited[x][y] = 1
            isMatch = backtrack(x-1, y, i+1) or backtrack(x+1, y, i+1) or backtrack(x, y-1, i+1) or backtrack(x, y+1, i+1)
            
            # uncheck this cell when backtracking
            visited[x][y] = 0
            return isMatch
        
        for r in range(m):
            for c in range(n):
                if backtrack(r, c, 0):
                    return True
        return False