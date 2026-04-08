class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # do BFS from the pacific shore and atlantic shore
        # the intersected cells are what we looking for
        m = len(heights)
        n = len(heights[0])
        q_pacific = deque()
        q_atlantic = deque()

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    q_pacific.append((i, j))
                if i == m-1 or j == n-1:
                    q_atlantic.append((i, j))


        def bfs(queue):
            reachable = set()
            while queue:
                x, y = queue.popleft()
                if (x, y) in reachable:
                    continue
                reachable.add((x, y))

                for dir_x, dir_y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = dir_x+x, dir_y+y
                    if 0 <= nx < m and 0 <= ny < n and heights[nx][ny] >= heights[x][y]:
                        queue.append((nx, ny))
            return reachable

        reachable_p = bfs(q_pacific)
        reachable_a = bfs(q_atlantic)
        return list(reachable_p & reachable_a)