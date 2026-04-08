class TreeNode:
    
    def __init__(self):
        self.nodeList = [None] * 26
        self.isWord = None

class Trie:

    def __init__(self):
        self.root = TreeNode()

    def add(self, word):
        curr = self.root
        for c in word:
            i = ord(c) - ord('a')
            if not curr.nodeList[i]:
                curr.nodeList[i] = TreeNode()
            curr = curr.nodeList[i]
        curr.isWord = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # make a word trie for words
        # when explore the board, it's easy to see if certain direction is worth exploring
        m = len(board)
        n = len(board[0])
        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        wordsTrie = Trie()
        for word in words:
            wordsTrie.add(word)
        
        # dfs
        def dfs(x, y, inPath, node):
            # base case: out of bound
            if x < 0 or x >= m or y < 0 or y >= n:
                return

            # base case: visited
            if (x, y) in inPath:
                return
            
            # not a valid prefix in trie
            char = board[x][y]
            index = ord(char) - ord('a')
            if node.nodeList[index] is None:
                return
            
            inPath.append((x, y))
            currNode = node.nodeList[index]

            # find a word, remove from trie to avoid repeating
            if currNode.isWord:
                ans.append(currNode.isWord)
                currNode.isWord = None
            
            # keep exploring
            for dir_x, dir_y in directions:
                nx, ny = dir_x + x, dir_y + y
                if 0 <= nx < m and 0 <= ny < n:
                    dfs(nx, ny, inPath, currNode)

            inPath.pop()

        

        # loop over the board
        ans = []
        for i in range(m):
            for j in range(n):
                dfs(i, j, [], wordsTrie.root)
        
        return ans