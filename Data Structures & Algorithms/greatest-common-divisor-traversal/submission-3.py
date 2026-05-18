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
        # build a graph: each num is a node, edge exists when they share gcd
        # check if the graph is connected as one component
        n = len(nums)
        uf = UnionFind(n)

        # time limit reached using nested loops
        # build a divisor dict to map divisor to original num to avoid repeat calculations
        divisor_to_num = defaultdict(int)
        for i in range(n):
            num = nums[i]

            # starting from 2 and increase until all primes are found
            divisor = 2
            while divisor * divisor <= num:
                if num % divisor == 0:  # find a divisor
                    if divisor not in divisor_to_num:
                        divisor_to_num[divisor] = i
                    else:   # a prev num has this divisor, share an edge
                        uf.union(i, divisor_to_num[divisor])

                        # break early
                        if uf.size == 1:
                            break
                    
                    # squeeze curr prime from num
                    while num % divisor == 0:
                        num //= divisor

                divisor += 1
            
            # check if there is a big prime at the end
            if num > 1:
                if num not in divisor_to_num:
                    divisor_to_num[num] = i
                else:   # a prev num has this divisor, share an edge
                    uf.union(i, divisor_to_num[num])
        
        return True if uf.size == 1 else False