class Solution:
    def numDecodings(self, s: str) -> int:
        # dp problem: O(n)
        # sanity check
        if s[0] == '0':
            return 0

        n = len(s)
        dp = [0] * (n+1)
        dp[0] = dp[1] = 1   # base case

        for i in range(2, n+1):
            # check single digit
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            
            # check double digits
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        
        return dp[n]