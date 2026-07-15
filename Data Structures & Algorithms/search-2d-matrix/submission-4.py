class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # single pass binary search: treat the matrix as one array
        m = len(matrix)
        n = len(matrix[0])
        l, r = 0, m * n - 1

        while l < r:
            mid = (l + r) // 2

            # convert array index to matrix index
            x, y = mid // n, mid % n
            if matrix[x][y] < target:
                l = mid + 1
            else:
                r = mid
        
        x, y = l // n, l % n
        return True if matrix[x][y] == target else False