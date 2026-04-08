class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # dp[i][j] = the longest path from (i, j)
        m = len(matrix)
        n = len(matrix[0])
        dp = [[1] * n for _ in range(m)]

        directions = [
            (-1, 0), 
            (1, 0),
            (0, -1),
            (0, 1)
        ]
        visited = [[False] * n for _ in range(m)]


        def dfs(node, parent_val):
            x, y = node[0], node[1]
            curr_val = matrix[x][y]
            # base case: invalid route
            if curr_val <= parent_val:
                return 0
            
            # visited node: return the explored path
            if visited[x][y]:
                return dp[x][y]
            
            visited[x][y] = True
            max_len = 1

            for dir_x, dir_y in directions:
                nx, ny = x + dir_x, y + dir_y
                if 0 <= nx < m and 0 <= ny < n:
                    curr_len = dfs((nx, ny), curr_val)
                    max_len = max(max_len, curr_len + 1)
            
            dp[x][y] = max_len
            return max_len

        
        # loop through the matrix
        max_path = 0
        for i in range(m):
            for j in range(n):
                curr_path = dfs((i, j), -1)
                max_path = max(max_path, curr_path)
        
        return max_path