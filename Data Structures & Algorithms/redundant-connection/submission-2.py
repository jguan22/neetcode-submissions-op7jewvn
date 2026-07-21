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
            return False
        
        if self.rank[rootx] > self.rank[rooty]:
            self.parent[rooty] = rootx
        elif self.rank[rootx] < self.rank[rooty]:
            self.parent[rootx] = rooty
        else:
            self.parent[rooty] = rootx
            self.rank[rootx] += 1
        
        self.size -= 1
        return True
        
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # use union find: O(E + V)
        n = len(edges)
        uf = UnionFind(n+1)

        for u, v in edges:
            if not uf.union(u, v):
                return [u, v]
        return None