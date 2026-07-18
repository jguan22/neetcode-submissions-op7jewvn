class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # greedy: go with larger stone first, use heap: O(n)
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)

        # pop two and smash until there is only one left or none: O(n * logn)
        while len(max_heap) > 1:
            s1 = heapq.heappop(max_heap)
            s2 = heapq.heappop(max_heap)

            remain = abs(s1 - s2)
            if remain > 0:
                heapq.heappush(max_heap, -remain)
            
        return 0 if len(max_heap) == 0 else -max_heap[0]