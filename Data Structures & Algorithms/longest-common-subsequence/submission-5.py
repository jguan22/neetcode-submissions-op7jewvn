class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 2d dp: O(m * n)
        m = len(text1)
        n = len(text2)
        dp = [[0] * (n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                # find a match, increment from prev subseq
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    # no match, choose the longest one
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[m][n]