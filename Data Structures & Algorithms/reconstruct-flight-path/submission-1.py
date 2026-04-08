class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for u, v in sorted(tickets, reverse=True):
            adj[u].append(v)
        itinerary = []

        def dfs(curr):
            while adj[curr]:
                next_dest = adj[curr].pop()
                dfs(next_dest)
            
            itinerary.append(curr)

        dfs("JFK")
        return itinerary[::-1]