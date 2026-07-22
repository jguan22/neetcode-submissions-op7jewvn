class Solution:
    def numDecodings(self, s: str) -> int:
        # edge case: leading 0
        if s[0] == '0':
            return 0
        
        # dp problem: O(n)
        n = len(s)
        dp = [0] * (n+1)
        
        # base case
        dp[0] = dp[1] = 1
        
        for i in range(2, n+1):
            # single digit
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            
            # double digits
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        return dp[n]