class TreeNode:

    def __init__(self):
        self.child = {}
        self.isWord = False


class WordDictionary:

    def __init__(self):
        self.root = TreeNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.child:
                curr.child[char] = TreeNode()
            curr = curr.child[char]
        
        curr.isWord = True


    def search(self, word: str) -> bool:
        n = len(word)
        
        def DFS(curr, index):
            if index == n:
                return curr.isWord
            
            if word[index] == '.':
                for child in curr.child.values():
                    if DFS(child, index + 1):
                        return True
                return False
            else:
                if word[index] not in curr.child:
                    return False
                return DFS(curr.child[word[index]], index + 1)

        return DFS(self.root, 0)
        
