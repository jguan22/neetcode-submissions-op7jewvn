class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # modified dijkstra
        adj = defaultdict(list)
        for u, v, w in flights:
            adj[u].append((v, w))

        dp = [float('inf')] * n
        heap = [(0, 0, src)]    # (cost, stops, node)
        while heap:
            curr_cost, stop, curr = heapq.heappop(heap)
            if curr == dst:
                return curr_cost

            if stop > k:
                continue

            if stop < dp[curr]:
                dp[curr] = stop
            else:
                continue

            for nei, cost in adj[curr]:
                heapq.heappush(heap, (curr_cost + cost, stop+1, nei))
        
        return -1