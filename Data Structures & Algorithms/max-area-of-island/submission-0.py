class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # keep track on the checked cells
        m = len(grid)
        n = len(grid[0])
        checked = [[False] * n for _ in range(m)]
        max_area = 0


        def DFS(x, y):
            # base case:
            if x >= m or x < 0 or y >= n or y < 0:
                return 0
            
            if checked[x][y]:
                return 0
            
            if grid[x][y] == 0:
                return 0
            
            # mark current land
            checked[x][y] = True

            # explore from here
            return DFS(x-1, y) + DFS(x+1, y) + DFS(x, y-1) + DFS(x, y+1) + 1
        


        for i in range(m):
            for j in range(n):
                if checked[i][j]:
                    continue
                if grid[i][j]:
                    max_area = max(max_area, DFS(i, j))
        
        return max_area