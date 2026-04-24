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
            self.rank[rootx] -= 1
        self.size -= 1
        return


class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        # build a graph where two nodes are connected if they share a non-1 divisor
        # convert to a graph problem: true if this graph only has one component
        divisor_map = defaultdict(int)  # map divisor to original num
        n = len(nums)
        uf = UnionFind(n)

        for i in range(n):
            curr = nums[i]
            divisor = 2
            while divisor * divisor <= curr:
                # find a prime
                if curr % divisor == 0:
                    if divisor not in divisor_map:
                        divisor_map[divisor] = i
                    else:
                        # find a path between curr num and pre num with this prime
                        uf.union(i, divisor_map[divisor])

                    # remove all divisor from curr num
                    while curr % divisor == 0:
                        curr //= divisor
                
                divisor += 1
            
            # last prime if remaining is bigger than 1
            if curr > 1:
                if curr not in divisor_map:
                    divisor_map[curr] = i
                else:
                    uf.union(i, divisor_map[curr])
        
        return uf.size == 1