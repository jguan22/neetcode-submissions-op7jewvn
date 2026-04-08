class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[i] = True if s[:i] can be segmented
        n = len(s)
        words = set(wordDict)
        dp = [False] * (n+1)
        dp[0] = True
        for i in range(1, n+1):
            for j in range(i):
                if s[j:i] in words and dp[j]:
                    dp[i] = True
        return dp[n]

