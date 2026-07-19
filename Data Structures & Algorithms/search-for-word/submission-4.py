class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # dfs to try each route: O(m * n* 3^L)
        m = len(board)
        n = len(board[0])
        l = len(word)
        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        # after first cell, each path has 3 directions to explore: O(3^L)
        def dfs(x, y, i):
            # base case: find the word
            if i == l:
                return True

            # base case: out of bound
            if x < 0 or x >= m or y < 0 or y >= n:
                return False

            # base case: visited or not match
            curr_letter = board[x][y]
            if curr_letter != word[i] or curr_letter == '#':
                return False

            # mark visited and keep exploring
            board[x][y] = '#'
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if dfs(nx, ny, i+1):
                    return True
            
            board[x][y] = curr_letter
            return False

        # explore the board: O(mn)
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False
