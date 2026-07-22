class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # build the graph: O(E)
        adj_list = defaultdict(list)
        for u, v, w in flights:
            adj_list[u].append((v, w))

        # use modified Dijkstra, starting from src: O(VklogVk)
        min_heap = [(0, 0, src)]     # (cost, stop, node)
        min_stops = [float('inf')] * n

        while min_heap:
            cost, stop, curr = heapq.heappop(min_heap)

            # base case:
            if curr == dst:
                return cost

            # skip if stop reach limit or more stops needed than prev run
            if stop >= min_stops[curr] or stop >= k+1:
                continue
            
            # continue if there is still chance to reach target less than k stops
            min_stops[curr] = stop

            for nxt, nxt_cost in adj_list[curr]:
                heapq.heappush(min_heap, (cost + nxt_cost, stop + 1, nxt))
        
        return -1