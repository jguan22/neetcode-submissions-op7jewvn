class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        res = []
        directions = [
            (0, 1), # right
            (1, 0), # down
            (0, -1), # left
            (-1, 0), # up
        ]
        dir_index = 0
        change_directions = 0
        x, y = 0, -1

        # use a visited set or flip in-place
        visited = [[False] * n for _ in range(m)]
        while change_directions < 4:
            dir_x, dir_y = directions[dir_index]
            while 1:
                nx, ny = x + dir_x, y + dir_y
                if nx < 0 or nx >= m or ny < 0 or ny >= n or visited[nx][ny]:
                    break
                
                # find a valid direction to go
                change_directions = 0
                x, y = nx, ny
                visited[x][y] = True
                res.append(matrix[x][y])
                
            change_directions += 1
            dir_index = (dir_index + 1) % 4

        return res