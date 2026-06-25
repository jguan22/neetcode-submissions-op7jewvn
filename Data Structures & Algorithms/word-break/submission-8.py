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

        # dfs with memo
        n = len(s)
        memo = set()

        # helper to search trie O(n^2)
        def dfs(start):
            # base case:
            if start == n:
                return True
            
            # explore this path before and not true
            if start in memo:
                return False
            
            curr = root
            for i in range(start, n):
                # dead end
                if s[i] not in curr:
                    break

                curr = curr[s[i]]

                # find a word, explore this path
                if '#' in curr:
                    if dfs(i+1):
                        return True

            # mark every dead end
            memo.add(start)
            return False

        # total runtime: O(WL + n^2)
        return dfs(0)