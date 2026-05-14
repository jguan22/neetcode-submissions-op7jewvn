class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # build a trie for fast query
        root = {}
        for word in dictionary:
            curr = root
            for c in word:
                if c not in curr:
                    curr[c] = {}
                curr = curr[c]
            curr['#'] = word
        
        # record possible word partitions
        dp = {}
        n = len(s)

        def backtrack(start):
            if start == n:
                return 0
            
            # early return when curr position was checked
            if start in dp:
                return dp[start]
            
            # 1. either skip curr letter
            min_extra = 1 + backtrack(start + 1)

            # 2. or try to use curr letter
            curr = root
            for end in range(start, n):
                if s[end] not in curr:
                    break

                curr = curr[s[end]]
                if '#' in curr:
                    min_extra = min(min_extra, backtrack(end + 1))
            
            # record curr min extra
            dp[start] = min_extra
            return min_extra
        

        return backtrack(0)