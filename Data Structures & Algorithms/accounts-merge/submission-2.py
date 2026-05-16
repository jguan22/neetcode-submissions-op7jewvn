class UnionFind:

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx == rooty:
            return
        
        if self.rank[rootx] > self.rank[rooty]:
            self.parent[rooty] = rootx
        elif self.rank[rooty] > self.rank[rootx]:
            self.parent[rootx] = rooty
        else:
            self.parent[rooty] = rootx
            self.rank[rootx] += 1
        return


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # use union find to merge nodes based on emails
        # nodes in same component belong to the same person
        n = len(accounts)
        uf = UnionFind(n)
        email_to_index = {}
        for i, account in enumerate(accounts):
            name = account[0]
            for email in account[1:]:
                # find a smae email, merge account
                if email in email_to_index:
                    uf.union(i, email_to_index[email])
                else:
                    email_to_index[email] = i
        
        # add emails to its parent account
        account_map = defaultdict(list)
        for email, index in email_to_index.items():
            parent_index = uf.find(index)
            account_map[parent_index].append(email)

        # prepare new accounts 
        new_accounts = []
        for index, email_list in account_map.items():
            new_account = [accounts[index][0]] + sorted(email_list)
            new_accounts.append(new_account)

        return new_accounts