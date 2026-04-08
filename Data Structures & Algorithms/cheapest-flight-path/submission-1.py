class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # bfs
        adj = defaultdict(list)
        for u, v, price in flights:
            adj[u].append((v, price))

        dp = [float('inf')] * n
        dp[src] = 0
        queue = deque([(src, 0)])

        while k >= 0:
            count = len(queue)
            for _ in range(count):
                curr, curr_cost = queue.popleft()
                for nei, price in adj[curr]:
                    new_cost = curr_cost + price
                    if new_cost < dp[nei]:
                        dp[nei] = new_cost
                        queue.append((nei, new_cost))
            k -= 1
        
        return dp[dst] if dp[dst] != float('inf') else -1