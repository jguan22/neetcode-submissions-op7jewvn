class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        directions = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0)
        ]

        visited = [[False] * n for _ in range(m)]
        x = y = 0
        visited[x][y] = True
        ordered_list = [matrix[0][0]]

        tried_dir = 0
        i = 0
        while tried_dir < 4:
            dir_x, dir_y = directions[i]
            while True:
                nx, ny = x + dir_x, y + dir_y
                if nx < 0 or nx >= m or ny < 0 or ny >= n or visited[nx][ny]:
                    break
            
                ordered_list.append(matrix[nx][ny])
                visited[nx][ny] = True
                x, y = nx, ny
                tried_dir = 0

            
            tried_dir += 1
            i = (i + 1) % 4
        
        return ordered_list