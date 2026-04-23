class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse=True)
        adj_list = defaultdict(list)
        for u, v in tickets:
            adj_list[u].append(v)
        
        ans = []

        def dfs(curr):
            while adj_list[curr]:
                nxt = adj_list[curr].pop()
                dfs(nxt)

            ans.append(curr)
            return
        
        dfs("JFK")
        return ans[::-1]