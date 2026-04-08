class UnionFind():

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.size = n
    
    def find(self, x):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return False
        
        if self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        elif self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1
        self.size -= 1
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # union find to form a tree
        heap = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                heapq.heappush(heap, (distance, i, j))
        
        uf = UnionFind(len(points))
        ans = 0
        while heap:
            distance, i, j = heapq.heappop(heap)

            # in the same component already
            if not uf.union(i, j):
                continue
            
            ans += distance
            if uf.size == 1:
                return ans
        
        return 0