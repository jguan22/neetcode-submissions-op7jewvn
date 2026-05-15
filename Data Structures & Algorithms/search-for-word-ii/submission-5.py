class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # build a trie for fast query
        root = {}
        for word in words:
            curr = root
            for c in word:
                if c not in curr:
                    curr[c] = {}
                curr = curr[c]
            
            # mark the leaf with word
            curr['#'] = word

        m = len(board)
        n = len(board[0])
        ans = []

        def search(x, y, parent):
            # block curr cell to avoid use it more than once
            curr_char = board[x][y]
            curr = parent[curr_char]
            board[x][y] = '*'
            
            # find a word and remove '#' to avoid duplicates
            if '#' in curr:
                ans.append(curr['#'])
                curr.pop('#')

            for dir_x, dir_y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dir_x, y + dir_y
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] in curr:
                    search(nx, ny, curr)
            
            # backtrack
            board[x][y] = curr_char

            # prune the leaf
            if not curr:
                parent.pop(curr_char)
            return


        for i in range(m):
            for j in range(n):
                if board[i][j] in root:
                    search(i, j, root)
        
        return ans