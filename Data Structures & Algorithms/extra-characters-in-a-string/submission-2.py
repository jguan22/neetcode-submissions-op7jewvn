class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # build a trie
        root = {}
        for word in dictionary:
            curr = root
            for c in word:
                if c not in curr:
                    curr[c] = {}
                curr = curr[c]
            curr['#'] = True
        
        # use a dp table to track result
        n = len(s)
        dp = {}

        def dfs(start):
            if start == n:
                return 0
            
            if start in dp:
                return dp[start]
            
            # either skip this letter
            minExtra = 1 + dfs(start + 1)

            # or include this letter
            curr = root
            for i in range(start, n):
                if s[i] not in curr:
                    break
                
                curr = curr[s[i]]

                # find a word, try to explore using it
                if '#' in curr:
                    minExtra = min(minExtra, dfs(i+1))
            
            dp[start] = minExtra
            return minExtra
        
        return dfs(0)

            