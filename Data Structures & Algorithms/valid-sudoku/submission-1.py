class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # need set for each row/col and each 3*3 cube
        rows = defaultdict(set)
        cols = defaultdict(set)
        cubes = defaultdict(set)

        n = len(board)
        for i in range(n):
            for j in range(n):
                if board[i][j] == ".":
                    continue
                
                num = board[i][j]
                if num in rows[i] or num in cols[j] or num in cubes[(i // 3, j // 3)]:
                    return False
                
                rows[i].add(num)
                cols[j].add(num)
                cubes[(i//3, j//3)].add(num)
        
        return True