class UnionFind():

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
    
    def find(self, x):
        if self.parent[x] == x:
            return x
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
        return


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # merge accounts if two have same email
        # union find: need to map email to account index then use index for union
        n = len(accounts)
        uf = UnionFind(n)
        email_to_acc = {}

        for i, acc in enumerate(accounts):
            for email in acc[1:]:
                # see this email before, union two accounts
                if email in email_to_acc:
                    uf.union(i, email_to_acc[email])
                else:   # add to map if not
                    email_to_acc[email] = i
        
        # prepare the ans
        accountList = defaultdict(list)
        for email, index in email_to_acc.items():
            # find its root in union and link to the account
            root = uf.find(index)
            accountList[root].append(email)
        
        ans = []
        for i, e in accountList.items():
            # name + sorted emails
            ans.append([accounts[i][0]] + sorted(e))
        return ans