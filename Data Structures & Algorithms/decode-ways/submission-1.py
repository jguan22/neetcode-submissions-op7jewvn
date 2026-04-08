class Solution:
    def numDecodings(self, s: str) -> int:
        # dp[i] = number of ways to decode s[:i+1]
        if s[0] == '0':
            return 0

        n = len(s)
        dp = [0] * (n+1)

        # base case: empty s has one way to decode, same as one char since we exclude the edge case
        dp[0] = dp[1] = 1
        
        for i in range(2, n+1):
            one = s[i-1]
            two = s[i-2:i]
            if one != '0':
                dp[i] += dp[i-1]
            if 10 <= int(two) <= 26:
                dp[i] += dp[i-2]
        
        return dp[n]