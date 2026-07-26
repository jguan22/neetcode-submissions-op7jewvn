class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # move (i, j) to (j, n-1-i) to (n-1-i, n-1-j) to (n-1-j, i)
        n = len(matrix)

        # loop through the board: O(n^2)
        for i in range((n+1)// 2):  # deal with odd n, the mid row only rotate once
            for j in range(n // 2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[n-1-j][i]
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
                matrix[j][n-1-i] = temp
        
        return
