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
        n = len(word)

        def dfs(start, curr):
            for i in range(start, n):
                if word[i] == '.':
                    for c in curr:
                        if c != '#' and dfs(i+1, curr[c]):
                            return True
                    return False

                if word[i] not in curr:
                    return False
                
                curr = curr[word[i]]
            
            return '#' in curr
        
        return dfs(0, self.root)