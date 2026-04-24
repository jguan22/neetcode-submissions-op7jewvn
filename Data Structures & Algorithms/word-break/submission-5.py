class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        dp = {}
        
        def dfs(start):
            if start >= n:
                return True
            
            if start in dp:
                return dp[start]
            
            for end in range(start+1, n+1):
                if s[start: end] in word_set:
                    if dfs(end):
                        dp[start] = True
                        return True
            
            dp[start] = False
            return False

        return dfs(0)