class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # build a trie for faster query
        root = {}
        for word in dictionary:
            curr = root
            for c in word:
                if c not in curr:
                    curr[c] = {}
                curr = curr[c]
            curr['#'] = word    # mark the end of word

        # dfs with memo
        n = len(s)
        memo = {}

        def dfs(start):
            # base case
            if start == n:
                return 0
            
            # return the best result from prev explore
            if start in memo:
                return memo[start]
            
            # two options: either use curr char or skip
            min_extra = 1 + dfs(start + 1)

            curr = root
            for end in range(start, n):
                # break early when no word to explore
                if s[end] not in curr:
                    break
                
                # explore it when find a word match
                curr = curr[s[end]]
                if '#' in curr:
                    min_extra = min(min_extra, dfs(end + 1))
            
            # record the curr result
            memo[start] = min_extra
            return min_extra
        
        
        return dfs(0)