class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # keep exploring until there is no out edge, add it to the route
        # sort the tickets backwards
        tickets.sort(reverse=True)

        # build the graph
        adj_list = defaultdict(list)
        for a, b in tickets:
            adj_list[a].append(b)
        
        itinerary = []


        def dfs(curr):
            # explore from curr nodes in lexical order
            while adj_list[curr]:
                # pop the edge once it is used
                nxt = adj_list[curr].pop()
                dfs(nxt)

            # add curr node once all edges are explored
            itinerary.append(curr)
        

        dfs('JFK')
        return itinerary[::-1]