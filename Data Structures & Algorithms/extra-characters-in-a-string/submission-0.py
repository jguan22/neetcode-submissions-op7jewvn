class Trie:

    def __init__(self):
        self.root = {}

    def add(self, word):
        curr = self.root
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        curr['#'] = True

    def search(self, word):
        curr = self.root
        for c in word:
            if c not in curr:
                return False
            curr = curr[c]
        return '#' in curr
    
    def startWith(self, prefix):
        curr = self.root
        for c in prefix:
            if c not in curr:
                return False
            curr = curr[c]
        return True

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # build a trie using dict
        trie = Trie()
        for word in dictionary:
            trie.add(word)
        n = len(s)

        # build a dp table to store pre search
        dp = {}
        
        def dfs(start):
            # base case
            if start >= n:
                return 0
            if start in dp:
                return dp[start]
            
            # either skip this char or use it to build word
            minExtra = 1 + dfs(start + 1)

            for i in range(start, n):
                if not trie.startWith(s[start:i+1]):
                    break
                elif trie.search(s[start:i+1]):
                    minExtra = min(minExtra, dfs(i+1))
            
            dp[start] = minExtra
            return minExtra
        
        return dfs(0)