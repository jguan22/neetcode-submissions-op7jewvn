class UnionFind():

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.size = n
    
    def find(self, x):
        if self.parent[x] != x:
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
        # convert to a building min spaning tree problem
        # add all edges to a min heap with dist: O(n^2)
        min_heap = []
        n = len(points)
        for i in range(n):
            for j in range(i+1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                min_heap.append((dist, i, j))
        
        # use union find
        uf = UnionFind(n) # O(n)
        heapq.heapify(min_heap) # O(n)
        total_weight = 0
        # worst case: pop until very last edge in the heap O(n^2 logn)
        while min_heap and uf.size > 1:
            dist, p1, p2 = heapq.heappop(min_heap)

            if not uf.union(p1, p2):
                continue
            
            total_weight += dist
        
        return total_weight
