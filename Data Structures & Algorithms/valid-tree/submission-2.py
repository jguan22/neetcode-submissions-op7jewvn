class UnionFind:

    def __init__(self, n):
        self.size = n
        self.parents = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx == rooty:  # cycle detected!
            return False
        
        if self.rank[rootx] > self.rank[rooty]:
            self.parents[rooty] = rootx
        elif self.rank[rootx] < self.rank[rooty]:
            self.parents[rootx] = rooty
        else:
            self.parents[rooty] = rootx
            self.rank[rootx] += 1
        self.size -= 1
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # check the numer of edges
        if len(edges) != n - 1:
            return False
            
        # valid tree means a graph with all nodes connected and no cycle
        # use union find: O(V)
        uf = UnionFind(n)

        # connect graph based on given edges: O(E), E is bounded by V in a valid tree (V-1)
        for u, v in edges:
            if not uf.union(u, v):
                return False
        
        return uf.size == 1