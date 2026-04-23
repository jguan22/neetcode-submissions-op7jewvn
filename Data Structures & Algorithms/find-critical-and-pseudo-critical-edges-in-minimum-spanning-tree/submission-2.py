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
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # critical edge: the one in all MSTs
        # pseudo edge: the one in some MSTs
        for i in range(len(edges)):
            edges[i].append(i)
        sorted_edges = sorted(edges, key=lambda x: x[2])

        def findMST(contain=-1, skip=-1):
            mst = 0
            uf = UnionFind(n)

            if contain != -1:
                a, b, w, _ = edges[contain]
                uf.union(a, b)
                mst += w

            for a, b, w, i in sorted_edges:
                if i == skip:
                    continue

                if uf.union(a, b):
                    mst += w
                    if uf.size == 1:
                        break
            
            return mst if uf.size == 1 else float('inf')
        
        # build the tree with and without a chosen edge to see if weight increases
        # critical edge increases, pseudo edge doesn't
        mst = findMST()
        critical = []
        pseudo = []
        for i in range(len(edges)):
            withEdge = findMST(contain=i)
            withoutEdge = findMST(skip=i)

            if withoutEdge > mst:
                critical.append(i)
            elif withEdge == mst:
                pseudo.append(i)
        
        return [critical, pseudo]
