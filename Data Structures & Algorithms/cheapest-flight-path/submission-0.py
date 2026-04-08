class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # use modified dijkstra (price, i, stop)
        adj_list = defaultdict(list)
        for u, v, price in flights:
            adj_list[u].append((v, price))
        
        # keep tracking (cost, node, stops)
        min_heap = [(0, src, -1)]
        # visited list to track stops
        visited = [float('inf')] * n
        while min_heap:
            cost, node, stops = heapq.heappop(min_heap)
            # base case: reach dst within k stops
            if node == dst and stops <= k:
                return cost
            
            # stop iterating if more than k stops
            if stops > k:
                continue
            
            # only update with less stops
            if stops >= visited[node]:
                continue

            visited[node] = stops
            for neigh, price in adj_list[node]:
                heapq.heappush(min_heap, (cost+price, neigh, stops+1))
        
        return -1  