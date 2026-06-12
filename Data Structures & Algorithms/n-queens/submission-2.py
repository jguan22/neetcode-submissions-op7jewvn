class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # backtrack: need to track rows, cols and both diag
        board = [['.'] * n for _ in range(n)]
        cols = set()
        pos_diags = set()
        neg_diags = set()
        sols = []

        def backtrack(r):
            # base case
            if r == n:
                sols.append(["".join(rows) for rows in board])
                return
            
            for c in range(n):
                if c not in cols and (r + c) not in pos_diags and (r - c) not in neg_diags:
                    # mark cell with queen and update all sets
                    board[r][c] = 'Q'
                    cols.add(c)
                    pos_diags.add(r + c)
                    neg_diags.add(r - c)
                    backtrack(r + 1)

                    # backtrack
                    board[r][c] = '.'
                    cols.remove(c)
                    pos_diags.remove(r + c)
                    neg_diags.remove(r - c)
        
        backtrack(0)
        return sols

