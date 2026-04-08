class Solution:
    def countSubstrings(self, s: str) -> int:
        # dp[i][j] = True if s[i:j+1] is a panlindrome
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        count = 0

        # two possible panlindrome: odd or even num
        # base case: single char
        for i in range(n):
            dp[i][i] = True
            count += 1
        
        # base case: double char
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                count += 1
        
        for size in range(3, n+1):
            for i in range(n - size + 1):
                j = i + size - 1

                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    count += 1
        
        return count