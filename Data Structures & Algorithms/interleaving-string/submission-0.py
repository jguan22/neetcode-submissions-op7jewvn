class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)
        l = len(s3)
        if m + n != l:
            return False

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
                # Option 1: Take character from s1
                take_from_s1 = dp[i-1][j] and s1[i-1] == s3[i+j-1]
                
                # Option 2: Take character from s2
                take_from_s2 = dp[i][j-1] and s2[j-1] == s3[i+j-1]
                
                dp[i][j] = take_from_s1 or take_from_s2


        return dp[m][n]