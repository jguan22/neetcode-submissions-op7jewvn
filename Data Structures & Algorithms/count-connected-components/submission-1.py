class UnionFind():

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.size = n

    def find(self, index):
        if self.parent[index] == index:
            return index
        # trace back to find the parent and compress the path
        self.parent[index] = self.find(self.parent[index])
        return self.parent[index]
    
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


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # use union find 
        union = UnionFind(n)
        for a, b in edges:
            union.union(a, b)
        
        return union.size