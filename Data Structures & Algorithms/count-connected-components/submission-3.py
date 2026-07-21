class UnionFind:

    def __init__(self, n):
        self.size = n
        self.parent = list(range(n))
        self.rank = [1] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx == rooty:
            return
        
        if self.rank[rootx] > self.rank[rooty]:
            self.parent[rooty] = rootx
        elif self.rank[rootx] < self.rank[rooty]:
            self.parent[rootx] = rooty
        else:
            self.parent[rooty] = rootx
            self.rank[rootx] += 1
        
        self.size -= 1
        return

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # use union find to connect nodes: O(E + V)
        uf = UnionFind(n)

        for u, v in edges:
            uf.union(u, v)
        
        return uf.size