class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # build a trie for given dict
        trie_root = {}
        for word in dictionary:
            curr = trie_root
            for char in word:
                if char not in curr:
                    curr[char] = {}
                curr = curr[char]
            curr['#'] = True
        
        # build a dp table to store search result
        dp = {}
        n = len(s)

        def dfs(start):
            if start >= n:
                return 0
            if start in dp:
                return dp[start]
            
            # option 1: skip this char
            minExtra = 1 + dfs(start + 1)

            # option 2: use this char
            curr = trie_root
            for i in range(start, n):
                # have to skip this char
                if s[i] not in curr:
                    break
                curr = curr[s[i]]

                # find a word, use it
                if '#' in curr:
                    minExtra = min(minExtra, dfs(i+1))
            
            # store the res
            dp[start] = minExtra
            return minExtra
        
        return dfs(0)

            