class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # use binary search
        m = len(matrix)
        n = len(matrix[0])

        # since the matrix is sorted, we can treat it as a single array
        l, r = 0, m * n - 1
        while l < r:
            mid = l + (r-l) // 2

            # convert mid to a cord in matrix
            x = mid // n
            y = mid % n

            if matrix[x][y] >= target:
                r = mid
            else:
                l = mid + 1

        return True if matrix[l // n][l % n] == target else False