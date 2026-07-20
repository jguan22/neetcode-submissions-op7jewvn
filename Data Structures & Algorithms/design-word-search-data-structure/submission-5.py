class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        # O(n)
        curr = self.root
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        curr['#'] = word

    def search(self, word: str) -> bool:
        # the worst case is all '.': O(26^n)
        # helper to search word in trie, easier to recursively search word with '.'
        n = len(word)
        def searchWord(start, curr):
            for i in range(start, n):
                c = word[i]
                # case of '.': search all possible child in curr trie node
                if c == '.':
                    for child in curr:
                        if child != '#' and searchWord(i+1, curr[child]):
                            return True
                    return False
                else:
                    if c not in curr:
                        return False
                    else:
                        curr = curr[c]
            return '#' in curr

        return searchWord(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)