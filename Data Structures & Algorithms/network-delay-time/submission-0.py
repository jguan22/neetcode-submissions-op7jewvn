class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # build the graph
        adj_list = defaultdict(list)
        for u, v, w in times:
            adj_list[u].append((v, w))
        
        # use Dijkstra
        dist_list = [float('inf')] * (n + 1)
        dist_list[k] = 0

        visited = set()
        min_heap = [(0, k)]

        while min_heap:
            dis, node = heapq.heappop(min_heap)
            # visited before or distance is shorter
            if node in visited:
                continue

            visited.add(node)

            if dis > dist_list[node]:
                continue

            for v, w in adj_list[node]:
                new_dis = dis + w
                if new_dis < dist_list[v]:
                    dist_list[v] = new_dis
                    heapq.heappush(min_heap, (new_dis, v))
        
        max_time = max(dist_list[1:])

        return max_time if max_time < float('inf') else -1