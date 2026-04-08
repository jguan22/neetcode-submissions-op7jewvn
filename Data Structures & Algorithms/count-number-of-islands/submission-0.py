class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # need to keep track on the checked cell
        m = len(grid)
        n = len(grid[0])
        checked = [[False] * n for _ in range(m)]
        count = 0

        
        def DFS(x, y):
            # base case: out of bound
            if x >= m or x < 0 or y >= n or y < 0:
                return
            # checked cell
            if checked[x][y] == True:
                return
            # reach a water cell
            if grid[x][y] == '0':
                return
            
            # mark current land cell
            checked[x][y] = True

            # check its neighbours
            DFS(x-1, y)
            DFS(x+1, y)
            DFS(x, y-1)
            DFS(x, y+1)
        

        # loop over all cells
        for i in range(m):
            for j in range(n):
                if checked[i][j]:
                    continue

                # explore from a land cell
                if grid[i][j] == '1':
                    DFS(i, j)
                    count += 1
        
        return count