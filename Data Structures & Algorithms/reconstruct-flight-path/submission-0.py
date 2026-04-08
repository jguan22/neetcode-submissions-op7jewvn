class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # sort the original list to ensure lexical order
        tickets.sort()
        ans = []

        # build the graph
        graph = defaultdict(list)
        for u, v in tickets:
            graph[u].append(v)
        

        def dfs(node):
            # base case: find ans
            if len(ans) == len(tickets) + 1:
                return True
            
            # base case: no way out
            if not graph[node]:
                return False
            
            # loop through neighbors based on lexical
            neighbors = list(graph[node])
            for i, neigh in enumerate(neighbors):
                # remove this edge from graph since it can't be used twice
                graph[node].pop(i)
                ans.append(neigh)
                
                if dfs(neigh):
                    return True

                # neigh is not the right route
                ans.pop()
                graph[node].insert(i, neigh)
            
            return False
        

        # run dfs
        ans.append("JFK")
        dfs("JFK")
        return ans