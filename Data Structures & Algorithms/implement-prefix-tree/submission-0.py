class TreeNode:

    def __init__(self):
        self.child = [None] * 26
        self.isWord = False


class PrefixTree:


    def __init__(self):
        self.root = TreeNode()
        

    def insert(self, word: str) -> None:
        curr = self.root
        # build the path
        for i in range(len(word)):
            index = ord(word[i]) - ord('a')
            if curr.child[index] is None:
                curr.child[index] = TreeNode()
            curr = curr.child[index]
        # mark the end
        curr.isWord = True
        

    def search(self, word: str) -> bool:
        curr = self.root
        for i in range(len(word)):
            index = ord(word[i]) - ord('a')
            if curr.child[index] is None:
                return False
            curr = curr.child[index]
        
        return curr.isWord
         

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i in range(len(prefix)):
            index = ord(prefix[i]) - ord('a')
            if curr.child[index] is None:
                return False
            curr = curr.child[index]
        
        return True
