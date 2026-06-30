class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # sanity check
        m = len(s1)
        n = len(s2)
        if m + n != len(s3):
            return False

        # since in 2D, each cell depends on its left or above
        # dp table only needs to store memo from prev row, 1D dp: O(n) space
        dp = [False] * (n+1)
        
        # base case:
        dp[0] = True    # empty string
        for j in range(1, n+1):     # match s2 to s3 to initialize first row
            if s2[j-1] == s3[j-1]:
                dp[j] = dp[j-1]

        # loop through s1 and s2: O(m*n)
        for i in range(1, m+1):
            # now match s1 to s3 for the first cell
            if s1[i-1] == s3[i-1] and dp[0]:
                dp[0] = True
            else:
                dp[0] = False
            
            # update current row in s2
            for j in range(1, n+1):
                # either from above: use char from s1
                if s1[i-1] == s3[i+j-1] and dp[j]:
                    dp[j] = True
                else:
                    dp[j] = False
                
                # or from left: use char from s2
                if s2[j-1] == s3[i+j-1]:
                    dp[j] |= dp[j-1]

        return dp[n]

        '''
        # sanity check
        m = len(s1)
        n = len(s2)
        if m + n != len(s3):
            return False

        # dp[i][j] = True if s1[:i] + s2[:j] can form s3[:i+j-1]
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # base case: empty string
        dp[0][0] = True

        for i in range(1, m+1):     # match s1 to s3
            if s1[i-1] == s3[i-1]:
                dp[i][0] = dp[i-1][0]
        
        for j in range(1, n+1):     # match s2 to s3
            if s2[j-1] == s3[j-1]:
                dp[0][j] = dp[0][j-1]
        
        # loop through s1 and s2: O(m*n)
        for i in range(1, m+1):
            for j in range(1, n+1):
                # either use char in s1
                if s1[i-1] == s3[i+j-1]:
                    dp[i][j] |= dp[i-1][j]
                
                # or use char in s2
                if s2[j-1] == s3[i+j-1]:
                    dp[i][j] |= dp[i][j-1]
        
        return dp[m][n]
        '''