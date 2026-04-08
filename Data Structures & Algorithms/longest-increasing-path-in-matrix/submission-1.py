class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # dp[i][j] = the longest path from (i, j)
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * n for _ in range(m)]

        def dfs(x, y):
            if dp[x][y] != 0:
                return dp[x][y]
            
            path = 1
            for dir_x, dir_y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = dir_x + x, dir_y + y
                if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] > matrix[x][y]:
                    path = max(path, dfs(nx, ny) + 1)
            
            dp[x][y] = path
            return path

        
        longest = 0
        for i in range(m):
            for j in range(n):
                longest = max(longest, dfs(i, j))
        return longest