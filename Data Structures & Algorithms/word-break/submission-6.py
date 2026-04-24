class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True    # base case
        for i in range(1, n+1):
            for j in range(i):
                if s[j:i] in word_set and dp[j]:
                    dp[i] = True
                    break
        
        return dp[n]