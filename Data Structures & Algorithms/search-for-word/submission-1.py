class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        directions = {
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        }
        visited = [[False] * n for _ in range(m)]

        def dfs(x, y, index):
            if index == len(word)-1 and board[x][y] == word[index]:
                return True
            
            if board[x][y] != word[index]:
                return False

            visited[x][y] = True
            for dir_x, dir_y in directions:
                nx, ny = dir_x + x, dir_y + y

                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    if dfs(nx, ny, index+1):
                        return True
            
            visited[x][y] = False
            return False
        

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        
        return False