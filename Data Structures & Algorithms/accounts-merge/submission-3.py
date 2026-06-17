class UnionFind:

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
    
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
            self.rank[rootx] += 1
        return


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # treat each account as a graph node, connect them based on the same email
        # at the end, each graph component is considered as one account; merge accounts based on it
        # use union find to do the merge
        uf = UnionFind(len(accounts))

        # use a dict to map email to account
        email_to_acc = defaultdict(int)
        for i, account in enumerate(accounts):
            for email in account[1:]:
                # email already exist, merge accounts
                if email in email_to_acc:
                    uf.union(i, email_to_acc[email])
                else:   # add email to dict
                    email_to_acc[email] = i
        
        # now map each email to its root account
        acc_map = defaultdict(list)
        for email, index in email_to_acc.items():
            parent_index = uf.find(index)
            acc_map[parent_index].append(email)

        # prepare new accounts and sort the email list
        new_accounts = []
        for index, email_list in acc_map.items():
            # name + sorted email list
            new_acc = [accounts[index][0]] + sorted(email_list)
            new_accounts.append(new_acc)

        return new_accounts