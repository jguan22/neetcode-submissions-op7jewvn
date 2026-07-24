class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # dp problem: O(m * n)
        m = len(matrix)
        n = len(matrix[0])
        dp = [[-1] * n for _ in range(m)]

        directions = [
            (-1, 0), 
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        def dfs(x, y):
            # base case: explore from this cell already
            if dp[x][y] != -1:
                return dp[x][y]
            
            curr_max = 1
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] > matrix[x][y]:
                    curr_max = max(curr_max, dfs(nx, ny) + 1)
            
            dp[x][y] = curr_max
            return curr_max
        
        # loop through the matrix
        max_path = 0
        for i in range(m):
            for j in range(n):
                curr_path = dfs(i, j)
                max_path = max(max_path, curr_path)
        
        return max_path