class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # sanity check
        if len(s1) + len(s2) != len(s3):
            return False
        
        # 2d dp problem: O(m*n)
        m = len(s1)
        n = len(s2)
        dp = [[False] * (n+1) for _ in range(m+1)]

        # base case
        dp[0][0] = True         # empty string
        for i in range(1, m+1):   # match s1 to s3
            if s1[i-1] == s3[i-1]:
                dp[i][0] = dp[i-1][0]
        
        for j in range(1, n+1):   # match s2 to s3
            if s2[j-1] == s3[j-1]:
                dp[0][j] = dp[0][j-1]
            
        for i in range(1, m+1):
            for j in range(1, n+1):
                # try to match char of s1 to s3
                if s1[i-1] == s3[i+j-1]:
                    dp[i][j] |= dp[i-1][j]

                # try to match char of s2 to s3
                if s2[j-1] == s3[i+j-1]:
                    dp[i][j] |= dp[i][j-1]
        
        return dp[m][n]