class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        # need to check the first col and row to find any 0
        firstCol = False
        for i in range(m):
            if matrix[i][0] == 0:
                firstCol = True
        
        firstRow = False
        for j in range(n):
            if matrix[0][j] == 0:
                firstRow = True

        # if a cell is 0, set the first cell in this row and col to 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        # set 0 if first row or col is 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # now, set first row and col if needed
        if firstCol:
            for i in range(m):
                matrix[i][0] = 0
        
        if firstRow:
            for j in range(n):
                matrix[0][j] = 0

        return
        