class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        while self.parent[x] != x:
            x = self.parent[x]
        return x
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
    
        if root_x == root_y:
            return
        
        # always choose the one with higher rank as parent
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # build a mini spanning tree
        n = len(points)
        uf = UnionFind(n)

        # need a min heap to track the weight of each edge (dist, (u, v))
        min_heap = []

        # add all edges
        for i in range(n):
            for j in range(i+1, n):
                u = points[i]
                v = points[j]
                dist = abs(u[0] - v[0]) + abs(u[1] - v[1])
                heapq.heappush(min_heap, (dist, (i, j)))

        # tree: n-1 edges plus no cycle
        count = 0
        ans = 0
        while count < n-1:
            dist, edge = heapq.heappop(min_heap)

            # add edge if not connected
            if uf.find(edge[0]) != uf.find(edge[1]):
                uf.union(edge[0], edge[1])
                ans += dist
                count += 1
            
        return ans