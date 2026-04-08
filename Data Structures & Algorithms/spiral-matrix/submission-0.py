class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        # move clockwise meaning changing direction in this order: right, down, left, up
        direction = 0
        directions = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0)
        ]
        
        visited = [[False] * n for _ in range(m)]
        change_direction = 0
        
        # set initial cell and direction
        x, y = 0, 0
        visited[x][y] = True
        ans = [matrix[0][0]]
        dir_x, dir_y = directions[direction]
        
        # move until no more direction to go
        while change_direction < 4:
            while True:
                # check if next cell is valid
                nx, ny = x + dir_x, y + dir_y
                if nx < 0 or nx > m-1 or ny < 0 or ny > n-1 or visited[nx][ny] == True:
                    break
                
                # add next valid cell
                x, y = nx, ny
                visited[x][y] = True
                ans.append(matrix[x][y])

                # reset the sign
                change_direction = 0
            
            # change direction
            change_direction += 1
            direction = (direction + 1) % 4
            dir_x, dir_y = directions[direction]


        return ans