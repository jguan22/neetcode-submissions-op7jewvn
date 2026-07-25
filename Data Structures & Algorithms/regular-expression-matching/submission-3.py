class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # dp problem: O(m*n)
        m = len(s)
        n = len(p)
        dp = [[False] * (n+1) for _ in range(m+1)]
        dp[0][0] = True     # base case

        # edge case for option 2 with leading '*': which is at 2nd position 'a*', 'a*b*'
        for j in range(2, n+1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, m+1):
            for j in range(1, n+1):
                # match with same char or '.'
                if p[j-1] == s[i-1] or p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    # option 1: we can use '*' to match if prev char matched
                    if p[j-2] == s[i-1] or p[j-2] == '.':
                        # check prev match result of dp[i-1][j] so we can extend as many as it needs
                        dp[i][j] = dp[i-1][j]
                    
                    # option 2: or we can skip it and prev char
                    dp[i][j] |= dp[i][j-2]
        
        return dp[m][n]
