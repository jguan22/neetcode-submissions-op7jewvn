class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # direction goes from right -> down -> left -> up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m, n = len(matrix), len(matrix[0])

        # track on curr direction and stop when all four dir checked at one cell
        curr_dir = 0
        checked_dir = 0
        x, y = 0, 0
        res = [matrix[0][0]]
        matrix[0][0] = '#'

        while checked_dir < 4:
            # keep moving on curr direction until out of bound or visited
            dx, dy = directions[curr_dir]
            while True:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] != '#':
                    res.append(matrix[nx][ny])
                    matrix[nx][ny] = '#'
                    x, y = nx, ny

                    # if there is at least one cell on the route, reset checked
                    checked_dir = 0
                else:
                    break
            
            # increment dir and checked dir
            checked_dir += 1
            curr_dir = (curr_dir + 1) % 4
        
        return res