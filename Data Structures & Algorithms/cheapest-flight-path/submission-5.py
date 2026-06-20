class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # use Dijkstra with some modifications
        # build the graph O(E)
        adj_list = defaultdict(list)
        for u, v, cost in flights:
            adj_list[u].append((v, cost))
        
        min_heap = [(0, src, 0)]     # need to store (cost, dst, stops)
        min_stops = [float('inf')] * n  # keep track on the min stops to reach each city

        # since the number of stops can range up to k
        # each node can be processed at most K + 1 times in the worst-case scenario
        while min_heap: # O(EklogEk)
            curr_cost, curr_city, num_stops = heapq.heappop(min_heap)
            if curr_city == dst:
                return curr_cost
            
            # skip if this route use k stops or use more stops than previous route
            if num_stops > k or num_stops >= min_stops[curr_city]:
                continue
            min_stops[curr_city] = num_stops

            for nxt, nxt_cost in adj_list[curr_city]:
                # not need to check visited, since higher cost with less stops may be the answer
                heapq.heappush(min_heap, (curr_cost + nxt_cost, nxt, num_stops + 1))

        return -1