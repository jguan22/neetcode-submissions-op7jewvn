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
            self.parent[rootx] = self.parent[rooty]
        elif self.rank[rootx] < self.rank[rooty]:
            self.parent[rooty] = self.parent[rootx]
        else:
            self.parent[rooty] = self.parent[rootx]
            self.rank[rootx] += 1
        self.size -= 1
        return True


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # use sorted list and UnionFind to build MST by using lightest edge first
        # critical edge is the one when skip it, total weight increases
        # pseudo is the one when skip it or force it, weight doesn't change
        edge_list = [(w, u, v, i) for i, (u, v, w) in enumerate(edges)]
        edge_list.sort()
        

        # helper to build MST excluding the index edge
        def buildMST(skip, force):
            uf = UnionFind(n)
            ans = 0
            # force the edge if any
            if force != -1:
                u, v, w = edges[force]
                uf.union(u, v)
                ans += w
            
            # build the MST under given condition
            for w, u, v, i in edge_list:
                if i == skip:
                    continue
                if uf.union(u, v):
                    ans += w

            return ans if uf.size == 1 else float('inf')


        # build a MST
        minWeight = buildMST(-1, -1)
        critical = []
        pseudo = []
        for i in range(len(edges)):
            # critical: skip it to increase MST
            if buildMST(i, -1) > minWeight:
                critical.append(i) 
            elif buildMST(-1, i) == minWeight:
                # pseudo: skip or force it, no change
                pseudo.append(i)
        return [critical, pseudo]