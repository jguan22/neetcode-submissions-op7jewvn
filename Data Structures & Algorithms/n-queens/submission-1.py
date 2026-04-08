class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # need three set to ensure each column and both diagnols only have one queen when iterating over rows
        col = set()

        # one has x+y as constant and the other has x-y as constant
        diag1 = set()
        diag2 = set()
        res = []
        board = [['.'] * n for _ in range(n)]

        def backtrack(r):
            if r >= n:
                ans = ["".join(col) for col in board]
                res.append(ans[:])
                return
            
            for c in range(n):
                if c not in col and (c+r) not in diag1 and (c-r) not in diag2:
                    col.add(c)
                    diag1.add(c+r)
                    diag2.add(c-r)
                    board[r][c] = 'Q'
                    backtrack(r+1)

                    # backtracking
                    board[r][c] = '.'
                    col.remove(c)
                    diag1.remove(c+r)
                    diag2.remove(c-r)
            
            return
        

        backtrack(0)
        return res