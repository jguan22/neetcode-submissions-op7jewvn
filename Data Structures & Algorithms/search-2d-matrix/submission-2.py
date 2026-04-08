class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # treat the matrix as a single array and use binary search
        m = len(matrix)
        n = len(matrix[0])

        l, r = 0, m * n - 1
        while l < r:
            mid = (l + r) // 2
            x, y = mid // n, mid % n
            if matrix[x][y] >= target:
                r = mid
            else:
                l = mid + 1
        
        a, b = l // n, l % n
        return matrix[a][b] == target