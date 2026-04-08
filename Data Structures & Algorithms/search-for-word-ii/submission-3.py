class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # build a dict for word list
        dict_root = {}
        for word in words:
            curr = dict_root
            for c in word:
                if c not in curr:
                    curr[c] = {}
                curr = curr[c]
            curr['#'] = word
        
        m = len(board)
        n = len(board[0])
        ans = []

        def dfs(x, y, parent):
            curr_c = board[x][y]
            curr = parent[curr_c]
            if '#' in curr:
                ans.append(curr['#'])
                curr.pop('#')
                
            
            # backtrack
            board[x][y] = '*'
            for dir_x, dir_y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dir_x, y + dir_y
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] in curr:
                    dfs(nx, ny, curr)
            board[x][y] = curr_c

            # Optimization: Trie Pruning
            # If the current node is now empty, remove it from the parent
            if not curr:
                parent.pop(curr_c)


        for i in range(m):
            for j in range(n):
                if board[i][j] in dict_root:
                    dfs(i, j, dict_root)
        return ans