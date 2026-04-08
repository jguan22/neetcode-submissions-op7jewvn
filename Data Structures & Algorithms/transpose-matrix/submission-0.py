class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        new_matrix = [[0] * m for _ in range(n)]

        for i in range(m):
            for j in range(n):
                new_matrix[j][i] = matrix[i][j]
        
        return new_matrix