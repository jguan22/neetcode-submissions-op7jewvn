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
        # critical edges: used to build MST. without it weight increase
        # pseudo-critical edges: can be used to build MST. without it wont increase the weight
        # other edges: cant be used to build MST
        # sort the edges by weight to build MST
        edge_list = [(w, i) for i, (_, _, w) in enumerate(edges)]
        edge_list.sort()

        def buildMST(force=None, skip=None):
            # use union find to build MST
            uf = UnionFind(n)
            weight = 0

            # add forced edge before building tree
            if force is not None:
                a, b, w = edges[force]
                uf.union(a, b)
                weight += w
            
            for w, i in edge_list:
                if i == force or i == skip:
                    continue
                
                # add curr edge if a, b are not connected yet
                a, b, w = edges[i]
                if uf.union(a, b):
                    weight += w
                
                # finish when all nodes are connected
                if uf.size == 1:
                    break
            
            # double check if a tree is formed
            return weight if uf.size == 1 else float('inf')


        mst = buildMST()
        critical = []
        pseudo = []
        for i in range(len(edges)):
            # if skip curr edge increases weight, it's critical
            if buildMST(skip=i) > mst:
                critical.append(i)
            # elif force doesnot increase, it's pseudo
            elif buildMST(force=i) == mst:
                pseudo.append(i)
        
        return [critical, pseudo]