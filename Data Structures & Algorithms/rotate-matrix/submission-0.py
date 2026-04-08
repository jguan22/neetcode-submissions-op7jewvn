class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # slice the matrix to quarters
        # switch each cell in this quarter with corresponding cells in other quarters
        n = len(matrix)

        # (i, j) -> (j, n-1-i) -> (n-1-i, n-1-j) -> (n-1-j, i)
        # (0, 1) -> (1, n-1) -> (n-1, n-2) -> (1, 0)
        for i in range(n//2):
            for j in range((n+1)//2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[n-1-j][i]
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
                matrix[j][n-1-i] = temp
        
        return