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
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        # gcd helper 
        def gcd(x, y):
            if x < y:
                x, y = y, x

            while True:
                remainder = x % y
                if remainder == 0:
                    return y
                x, y = y, remainder
        
        # loop over every pairs in the list to form graph
        edges = []
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if gcd(nums[i], nums[j]) > 1:
                    edges.append((i, j))
        
        uf = UnionFind(n)
        for u, v in edges:        
            uf.union(u, v)
        return uf.size == 1