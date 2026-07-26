class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # use first row and col as indicator to mark whether each col should be 0
        m = len(matrix)
        n = len(matrix[0])

        # first pass on frist row and col to determine if it should be 0
        first_row = False
        for j in range(n):
            if matrix[0][j] == 0:
                first_row = True
                break
        
        first_col = False
        for i in range(m):
            if matrix[i][0] == 0:
                first_col = True
                break
        
        # second pass to loop through the rest of the board: O(m * n)
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # third pass to turn rows and cols to 0: O(m * n)
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # check if need to turn first row and col
        if first_col:
            for i in range(m):
                matrix[i][0] = 0
        if first_row:
            for j in range(n):
                matrix[0][j] = 0
        return