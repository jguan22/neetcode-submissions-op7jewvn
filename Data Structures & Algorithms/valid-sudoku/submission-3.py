class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # need to track each row, each column, and each box
        rows = defaultdict(set)
        cols = defaultdict(set)

        # each box use tuple with row and col num divide by 3
        boxes = defaultdict(set)

        # loop through 9 * 9 board: O(1)
        for r in range(9):
            for c in range(9):
                num = board[r][c]

                # skip empty ones
                if num == '.':
                    continue

                if num in rows[r] or num in cols[c] or num in boxes[(r//3, c//3)]:
                    return False
                
                rows[r].add(num)
                cols[c].add(num)
                boxes[(r//3, c//3)].add(num)
            
        
        return True