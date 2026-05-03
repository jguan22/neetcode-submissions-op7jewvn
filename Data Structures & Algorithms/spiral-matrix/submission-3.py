class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # run right, down, left, up until all four dir cannot be extended at the same cell
        m = len(matrix)
        n = len(matrix[0])
        directions = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0)
        ]

        visited = [[False] * n for _ in range(m)]
        x, y = 0, 0
        res = [matrix[x][y]]
        visited[x][y] = True

        checked_dir = 0
        i = 0
        while checked_dir < 4:
            dir_x, dir_y = directions[i]

            # keep moving on curr direction until out of bound or visited
            while True:
                nx, ny = dir_x + x, dir_y + y
                if nx < 0 or nx >= m or ny < 0 or ny >= n or visited[nx][ny]:
                    break

                visited[nx][ny] = True
                res.append(matrix[nx][ny])
                x, y = nx, ny

                # reset if there is at least one available cell in curr dir
                checked_dir = 0
            
            checked_dir += 1
            i = (i + 1) % 4

        return res   