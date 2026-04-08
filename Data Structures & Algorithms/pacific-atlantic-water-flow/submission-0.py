class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # do BFS from the pacific shore and atlantic shore
        # the intersected cells are the answer 
        m = len(heights)
        n = len(heights[0])
        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        # x = 0 and y = 0: pacific
        # x = m-1 and y = n-1: atlantic
        q_pacific = deque()
        q_atlantic = deque()
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    q_pacific.append((i, j))
                if i == m-1 or j == n-1:
                    q_atlantic.append((i, j))
        

        def BFS(queue):
            cell_set = set()
            while queue:
                x, y = queue.popleft()
                cell_set.add((x, y))
                height = heights[x][y]
                for dir_x, dir_y in directions:
                    nx, ny = x+dir_x, y+dir_y
                    if 0 <= nx < m and 0 <= ny < n and heights[nx][ny] >= height and (nx, ny) not in cell_set:
                        queue.append((nx, ny))
            
            return cell_set

       
        pacific_set = BFS(q_pacific)
        atlantic_set = BFS(q_atlantic)
        return list(pacific_set & atlantic_set)