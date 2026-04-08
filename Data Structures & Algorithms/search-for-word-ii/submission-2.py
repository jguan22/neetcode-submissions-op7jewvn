class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # make a word trie for words
        trie = {}
        for word in words:
            curr = trie
            for c in word:
                if c not in curr:
                    curr[c] = {}
                curr = curr[c]
            curr['#'] = word

        m = len(board)
        n = len(board[0])
        res = []
        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        def dfs(x, y, parent):
            char = board[x][y]
            curr = parent[char]

            # mute the board (use it as a visited set)
            board[x][y] = '*'

            # find a word, pop it so we dont have duplicates in res
            word_found = curr.pop('#', None)
            if word_found:
                res.append(word_found)

            for dir_x, dir_y in directions:
                nx, ny = x + dir_x, y + dir_y
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] in curr:
                    dfs(nx, ny, curr)

            # backtracking
            board[x][y] = char

            # once done searching this branch, prune it to avoid revisit it again
            if not curr:
                parent.pop(char)

        
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    dfs(i, j, trie)
        return res