class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # build a trie for fast search
        root = {}
        for word in words:
            curr = root
            for c in word:
                if c not in curr:
                    curr[c] = {}
                curr = curr[c]
            curr['#'] = word
        
        m = len(board)
        n = len(board[0])
        ans = []

        def dfs(x, y, parent):
            curr_letter = board[x][y]
            curr = parent[curr_letter]

            board[x][y] = '*'

            if '#' in curr:
                ans.append(curr['#'])
                curr.pop('#')
            
            for dir_x, dir_y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = dir_x + x, dir_y + y
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] in curr:
                    dfs(nx, ny, curr)
            
            board[x][y] = curr_letter

            if not curr:
                parent.pop(curr_letter)


        for i in range(m):
            for j in range(n):
                if board[i][j] in root:
                    dfs(i, j, root)
        return ans