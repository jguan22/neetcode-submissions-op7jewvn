class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Dijkstra
        adj = defaultdict(list)
        for i, (u, v, w) in enumerate(times):
            adj[u].append((v, w))

        heap = [(0, k)]  # time, dest
        res = {}
        res[k] = float('inf')

        while heap:
            curr_cost, dest = heapq.heappop(heap)
            if curr_cost >= res.get(dest, float('inf')):
                continue
            res[dest] = curr_cost
            
            if len(res) == n:
                return curr_cost
            
            for nei, cost in adj[dest]:
                heapq.heappush(heap, (curr_cost + cost, nei))
        
        return -1