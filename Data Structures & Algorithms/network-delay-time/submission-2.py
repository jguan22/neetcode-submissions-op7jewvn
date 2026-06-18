class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # build the graph
        adj_list = defaultdict(dict)
        for u, v, w in times:
            adj_list[u][v] = w

        # Dijkstra
        min_heap = [(0, k)]     # (cost, node)
        visited = set()
        total_cost = 0

        # loop until all nodes are visited or there is no edge left to explore
        while min_heap and len(visited) < n:
            cost, curr = heapq.heappop(min_heap)

            if curr in visited:
                continue
            visited.add(curr)

            # mark total cost and keep exploring from curr node
            total_cost = max(total_cost, cost)
            for nxt in adj_list[curr]:
                nxt_cost = cost + adj_list[curr][nxt]
                heapq.heappush(min_heap, (nxt_cost, nxt))
        
        return total_cost if len(visited) == n else -1