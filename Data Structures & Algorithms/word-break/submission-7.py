class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)
        dp = {}

        def dfs(start):
            if start == n:
                return True
            
            if start in dp:
                return dp[start]
            
            for end in range(start, n):
                # check if substring is in dict
                if s[start:end+1] in wordSet:
                    # find a valid word, explore it
                    if dfs(end+1):
                        # once it's true return true, no need to memo it
                        return True

            # memo invalid path  
            dp[start] = False
            return False
        
        return dfs(0)