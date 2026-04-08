class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # use binary search
        # treat the matrix as one array
        m = len(matrix)
        n = len(matrix[0])

        lo = 0 
        hi = m * n - 1
        
        while lo <= hi:
            mid = (lo + hi) // 2

            # convert the index into row and col
            row = mid // n
            col = mid % n

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        
        return False