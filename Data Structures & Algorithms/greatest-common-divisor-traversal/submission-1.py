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
        # Connect via Prime Factors
        primeList = {}
        n = len(nums)
        uf = UnionFind(n)

        for i in range(n):
            # find prime factors of each number
            temp = nums[i]
            d = 2
            while d * d <= temp:
                # find a prime
                if temp % d == 0:
                    # put it to the dict or union it with previous num has this prime
                    if d not in primeList:
                        primeList[d] = i
                    else:
                        uf.union(i, primeList[d])

                    # squeeze all ds in num
                    while temp % d == 0:
                        temp //= d
                d += 1
            
            # the remainning is a prime too
            if temp > 1:
                if temp not in primeList:
                    primeList[temp] = i
                else:
                    uf.union(i, primeList[temp])

        return uf.size == 1