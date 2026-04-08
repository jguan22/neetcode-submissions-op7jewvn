class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        curr['#'] = True

    def search(self, word: str) -> bool:
        # dfs helper
        def dfs(start, node):
            curr = node
            for i in range(start, len(word)):
                if word[i] in curr:
                    curr = curr[word[i]]
                elif word[i] == '.':
                    for child in curr:
                        if child != "#" and dfs(i+1, curr[child]):
                            return True
                    return False
                else:
                    return False
            
            # once reach the end of word
            return '#' in curr
        
        return dfs(0, self.root)
