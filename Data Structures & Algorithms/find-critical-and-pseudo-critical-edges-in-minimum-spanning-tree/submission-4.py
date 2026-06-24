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
        rootx, rooty = self.find(x), self.find(y)
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
        # critical edges: always in MST, weight increases without
        # pseudo edges: can be in some MST not all, weight no change without
        # sort the edge based on weight to start building MST from lighter edge: O(ElogE)
        edge_list = [(w, i) for i, (_, _, w) in enumerate(edges)]
        edge_list.sort()

        # helper to build mst O(E)
        def buildMST(include=None, exclude=None):
            # use union find to build MST
            uf = UnionFind(n)
            total_w = 0

            # add force include edge
            if include is not None:
                a, b, w = edges[include]
                total_w += w
                uf.union(a, b)

            # build mst from lighter edges
            for _, i in edge_list:
                # skip force or skip edge
                if i == include or i == exclude:
                    continue
                
                a, b, w = edges[i]
                if uf.union(a, b):
                    total_w += w
                
                # base case: tree is formed
                if uf.size == 1:
                    break

            # edge case: can't form a tree, return inf weight
            return total_w if uf.size == 1 else float('inf')


        critical = []
        pseudo = []
        mst = buildMST()
        # loop through all edges: O(E^2)
        for i in range(len(edges)):
            # build the tree without curr edge: critical if w increase
            if buildMST(None, i) > mst:
                critical.append(i)
            # build the tree with curr edge forced: pseudo if not increase
            elif buildMST(i, None) == mst:
                pseudo.append(i)
        
        return [critical, pseudo]