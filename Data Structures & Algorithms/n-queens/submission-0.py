class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # only one queen in each row and col
        # also, only one queen in each diagnal
        # meaning we only need to loop over one row
        col = set()

        # each diagnal with positive slope has same sum
        posDiag = set()
        # each diagnal with negative slope has same diff
        negDiag = set()

        ans = []
        board = [["."] * n for _ in range(n)]

        def backtrack(r):
            # base case
            if r == n:
                res = ["".join(row) for row in board]
                ans.append(res)
                return
            
            for c in range(n):
                # this col is taken
                if c in col:
                    continue
                
                # this diagnal is taken
                if (r + c) in posDiag or (r - c) in negDiag:
                    continue
                
                # choose this cell and update the board
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = "Q"

                # go to next row
                backtrack(r+1)

                # recover the board
                board[r][c] = "."
                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
            
        # starting from the first row
        backtrack(0)
        return ans