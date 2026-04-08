class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])
        min_heap = [(0, 0, 0)]
        visited = [[False] * cols for _ in range(rows)]
        min_effort = 0

        while min_heap:
            curr_effort, x, y = heapq.heappop(min_heap)
            if visited[x][y]:
                continue

            visited[x][y] = True
            min_effort = max(min_effort, curr_effort)

            if x == rows - 1 and y == cols - 1:
                return min_effort

            for dir_x, dir_y in [(1, 0 ), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = dir_x + x, dir_y + y
                if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny]:
                    nxt_effort = abs(heights[nx][ny] - heights[x][y])
                    heapq.heappush(min_heap, (nxt_effort, nx, ny))
            
        return min_effort