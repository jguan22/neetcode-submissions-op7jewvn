class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[i] = True if s[:i] can be segmented
        n = len(s)
        dp = [False] * (n+1)

        # base case
        dp[0] = True

        word_set = set(wordDict)
        for i in range(1, n+1):
            for word in word_set:
                if i < len(word):
                    continue
                
                start = i - len(word)
                if s[start:i] == word and dp[start] == True:
                    dp[i] = True
                    break
            
        return dp[n]

