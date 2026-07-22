class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # build the adjacent list for the graph
        adj_list = defaultdict(dict)
        for u, v, w in times:
            adj_list[u][v] = w
        
        # use Dijkstra, starting from node k
        min_heap = [(0, k)]
        visited = set()

        while min_heap:
            cost, curr = heapq.heappop(min_heap)

            if curr in visited:
                continue
            visited.add(curr)

            if len(visited) == n:
                return cost

            for nxt in adj_list[curr]:
                heapq.heappush(min_heap, (cost + adj_list[curr][nxt], nxt))
        
        return -1

        