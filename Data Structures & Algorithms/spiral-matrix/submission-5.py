class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # the direction goes in order as [right, down, left up]
        directions = [
            (0, 1), 
            (1, 0), 
            (0, -1),
            (-1, 0)
        ]
        m = len(matrix)
        n = len(matrix[0])
        res = [matrix[0][0]]
        matrix[0][0] = '#'

        # loop through the matrix starting from (0, 0): O(m*n)
        x, y = 0, 0
        dir_i = 0
        checked = 0
        while checked < 4:
            # keep going curr direction until out of bound or visited
            dir_x, dir_y = directions[dir_i]
            while True:
                nx, ny = x + dir_x, y + dir_y
                if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] != '#':
                    res.append(matrix[nx][ny])
                    matrix[nx][ny] = '#'

                    x, y = nx, ny

                    # reset checked direction to 0 if there is at least one cell on this dir
                    checked = 0
                else:
                    break
                
            # increment checked direction and curr direction index
            checked += 1
            dir_i = (dir_i + 1) % 4
        
        return res