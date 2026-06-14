class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # build trie for faster query
        root = {}
        for word in words:
            curr = root
            for c in word:
                if c not in curr:
                    curr[c] = {}
                curr = curr[c]
            curr['#'] = word    # mark the end of word
        
        # search the board
        m = len(board)
        n = len(board[0])
        ans = []

        def dfs(x, y, parent):
            # check if curr route is available and mark board as used
            if board[x][y] not in parent:
                return

            c = board[x][y]
            board[x][y] = '.'
            curr = parent[c]

            # base case
            if '#' in curr:
                ans.append(curr['#'])
                curr.pop('#')

            # explore all directions
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] != '.':
                    dfs(nx, ny, curr)
            
            board[x][y] = c

            # prune the branch
            if not curr:
                parent.pop(c)
            return


        for i in range(m):
            for j in range(n):
                dfs(i, j, root)
        
        return ans