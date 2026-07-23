class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # search with trie O(W * L), where W is num of words and L is average length
        root = {}
        for word in wordDict:
            curr = root
            for c in word:
                if c not in curr:
                    curr[c] = {}
                curr = curr[c]
            curr['#'] = word

        # dfs with memo to store prev branch
        n = len(s)
        memo = {}
        
        # helper dfs method: worst case n char and each loop n times O(n^2)
        def dfs(start):
            # base case
            if start >= n:
                return True

            if start in memo:
                return False
            
            curr = root
            for i in range(start, n):
                # no route on this branch
                if s[i] not in curr:
                    break
                
                curr = curr[s[i]]
                if '#' in curr: # keep exploring from a word
                    if dfs(i+1):
                        return True
            
            # record curr trial
            memo[start] = False
            return False

        # total runtime: O(WL + n^2)
        return dfs(0)
