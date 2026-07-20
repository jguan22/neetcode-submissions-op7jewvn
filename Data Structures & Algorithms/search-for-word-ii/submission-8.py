class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # use trie to store all words: O(W*L), where W is num of words and L is len
        root = {}
        for word in words:
            curr = root
            for c in word:
                if c not in curr:
                    curr[c] = {}
                curr = curr[c]

            # store the word at the end
            curr['#'] = word
        
        m = len(board)
        n = len(board[0])
        res = []
        
        # backtracking the route starting at given cell: O(3^L)
        def backtrack(x, y, parent):
            # check if curr route is available and mark board as used
            if board[x][y] not in parent:
                return
            char = board[x][y]
            board[x][y] = '.'
            curr = parent[char]

            # add any word and prune the trie
            if '#' in curr:
                res.append(curr['#'])
                curr.pop('#')

            # explore all directions
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] != '.':
                    backtrack(nx, ny, curr)
            
            # backtrack
            board[x][y] = char

            # prune the branch
            if not curr:
                parent.pop(char)


        # loop through all cells in board: O(n * m * 3^L)
        for i in range(m):
            for j in range(n):
                backtrack(i, j, root)

        return res