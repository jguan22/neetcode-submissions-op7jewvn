class PrefixTree:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        # loop through the word: O(n)
        curr = self.root
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        # use # to represent end of word
        curr['#'] = True

    def search(self, word: str) -> bool:
        # loop through the word: O(n)
        curr = self.root
        for c in word:
            if c not in curr:
                return False
            curr = curr[c]
        return '#' in curr

    def startsWith(self, prefix: str) -> bool:
        # loop through the word: O(n)
        curr = self.root
        for c in prefix:
            if c not in curr:
                return False
            curr = curr[c]
        return True
        
        