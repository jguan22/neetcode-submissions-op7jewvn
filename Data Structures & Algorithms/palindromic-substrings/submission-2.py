class Solution:
    def countSubstrings(self, s: str) -> int:
        # 2d dp problem: O(n^2)
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        count = 0
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if j-i <= 1:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                    
                    if dp[i][j]:
                        count += 1
        return count