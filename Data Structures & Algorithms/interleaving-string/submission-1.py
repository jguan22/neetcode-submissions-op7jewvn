class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)
        l = len(s3)
        # sanity check
        if m+n != l:
            return False

        # dp[i][j] = True if s1[:i] + s2[:j] == s3[:i+j]
        dp = [[False] * (n+1) for _ in range(m+1)]
        # base case
        dp[0][0] = True
        for i in range(1, m+1):
            if s1[i-1] == s3[i-1]:
                dp[i][0] = dp[i-1][0]
        for j in range(1, n+1):
            if s2[j-1] == s3[j-1]:
                dp[0][j] = dp[0][j-1] 
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s1[i-1] == s3[i+j-1] and dp[i-1][j]:
                    dp[i][j] = True
                if s2[j-1] == s3[i+j-1] and dp[i][j-1]:
                    dp[i][j] = True
        
        return dp[m][n]