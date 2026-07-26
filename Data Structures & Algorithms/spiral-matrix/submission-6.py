class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # the direction goes in order as [right, down, left, up]
        directions = [
            (0, 1), 
            (1, 0), 
            (0, -1),
            (-1, 0)
        ]
        m = len(matrix)
        n = len(matrix[0])
        res = []
        
        checked_dir = 0
        dir_i = 0
        x, y = 0, -1        # start from the one on the left of (0, 0)

        # explore until all four directions are checked in a single cell
        while checked_dir < 4:
            # keep explore curr direction
            dx, dy = directions[dir_i]
            while True:
                nx, ny = x + dx, y + dy

                # stop curr direction if out of bound or visited
                if nx < 0 or nx >= m or ny < 0 or ny >= n or matrix[nx][ny] == '#':
                    break

                # add res and mark visited
                x, y = nx, ny
                res.append(matrix[x][y])
                matrix[x][y] = '#'

                # reset the checked if at least one cell checked
                checked_dir = 0
            
            dir_i = (dir_i + 1) % 4
            checked_dir += 1
        
        # loop through the board: O(m*n)
        return res
                