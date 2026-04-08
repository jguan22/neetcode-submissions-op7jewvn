class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        diag1 = set()   # r+c
        diag2 = set()   # r-c
        
        def backtrack(r):
            if r >= n:
                return 1
            
            count = 0
            for c in range(n):
                if c not in col and r+c not in diag1 and r-c not in diag2:
                    col.add(c)
                    diag1.add(r+c)
                    diag2.add(r-c)
                    count += backtrack(r+1)

                    col.remove(c)
                    diag1.remove(r+c)
                    diag2.remove(r-c)
            return count

            
        return backtrack(0)