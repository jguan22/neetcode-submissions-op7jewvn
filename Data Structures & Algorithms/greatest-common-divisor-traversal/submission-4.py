class UnionFind:

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.size = n
    
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
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        # convert to a graph problem: each num is a node, common divisors as edges
        # union find to do graph component merging
        n = len(nums)
        uf = UnionFind(n)

        # use a dict to map divisors to nums
        divisor_map = defaultdict(int)

        # loop through all nums and find all divisors of each: O(n * sqr(m))
        for i, num in enumerate(nums):
            curr = num
            d = 2
            while d * d <= num:
                # find a divisor
                if curr % d == 0:
                    if d in divisor_map:
                        uf.union(i, divisor_map[d])
                    else:
                        divisor_map[d] = i
                
                    # squeeze out curr d
                    while curr % d == 0:
                        curr //= d
                
                # early break
                if uf.size == 1:
                    return True

                # check next divisor
                d += 1

            # check last potential divisor
            if curr > 1:    
                if curr in divisor_map:
                    uf.union(i, divisor_map[curr])
                else:
                    divisor_map[curr] = i
        
        # graph is connected if size of graph component is 1
        return True if uf.size == 1 else False