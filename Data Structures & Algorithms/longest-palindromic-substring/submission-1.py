class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dp[i][j] = substring[i:j+1] is panlindrome or not
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        longest = s[0]
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    if j-i == 1 or dp[i+1][j-1]:
                        dp[i][j] = True
                        if j-i+1 > len(longest):
                            longest = s[i:j+1]
                        
        return longest