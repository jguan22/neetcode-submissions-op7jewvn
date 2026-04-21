class UnionFind:

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        if self.find(x) == self.find(y):
            return 
        
        rootx = self.find(x)
        rooty = self.find(y)

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
        # use union find to do merge
        # use dict to map each email to account index
        n = len(accounts)
        uf = UnionFind(n)
        email_to_account = {}

        for i, account in enumerate(accounts):
            for email in account[1:]:
                # email already exist, merge account
                if email in email_to_account:
                    uf.union(i, email_to_account[email])
                else:   # not exist, mark index
                    email_to_account[email] = i

        # add all emails to its parent
        account_dict = defaultdict(list)
        for email, index in email_to_account.items():
            parent_index = uf.find(index)
            account_dict[parent_index].append(email)

        # sort the email lists and add account name
        new_accounts = []
        for index, email_list in account_dict.items():
            name = accounts[index][0]
            new_accounts.append([name] + sorted(email_list))
        
        return new_accounts