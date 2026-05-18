class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # build graph
        tickets.sort(reverse=True)
        adj_list = defaultdict(list)
        for u, v in tickets:
            adj_list[u].append(v)
        
        # explore all paths and build the route backwards
        # a node must be the last stop when there is no outgoing edges
        itinerary = []

        def dfs(curr):
            # pop edges while exploring all neighbors
            while adj_list[curr]:
                nxt = adj_list[curr].pop()
                dfs(nxt)

            # add curr node when no edges left
            itinerary.append(curr)

        dfs("JFK")
        return itinerary[::-1]