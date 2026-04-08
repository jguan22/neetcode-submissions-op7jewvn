class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # 2d prefix sum
        m = len(matrix)
        n = len(matrix[0])
        self.prefix_sum = [[0] * (n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            curr_sum = 0
            for j in range(1, n+1):
                curr_sum += matrix[i-1][j-1]
                self.prefix_sum[i][j] = self.prefix_sum[i-1][j] + curr_sum


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        region1 = self.prefix_sum[row2+1][col2+1]
        region2 = self.prefix_sum[row1][col2+1]
        region3 = self.prefix_sum[row2+1][col1]
        region4 = self.prefix_sum[row1][col1]
        return region1 - region2 - region3 + region4