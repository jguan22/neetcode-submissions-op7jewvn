class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # dp[i][j] = True if s1[:i] + s2[:j] can make s3[:i+j-1]
        m = len(s1)
        n = len(s2)
        if m + n != len(s3):
            return False
            
        dp = [[False] * (n+1) for _ in range(m+1)]

        # base case
        dp[0][0] = True     # empty string
        for i in range(1, m+1):     # match s1 to s3
            if s1[i-1] == s3[i-1]:
                dp[i][0] = dp[i-1][0]

        for j in range(1, n+1):     # match s2 to s3
            if s2[j-1] == s3[j-1]:
                dp[0][j] = dp[0][j-1]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                # use s1[i] as next char
                if s1[i-1] == s3[i+j-1] and dp[i-1][j] == True:
                    dp[i][j] = True

                # use s2[j] as next char
                if s2[j-1] == s3[i+j-1] and dp[i][j-1] == True:
                    dp[i][j] = True
                
        return dp[m][n]