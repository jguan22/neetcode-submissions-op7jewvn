class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # use min_heap: O(n)
        min_heap = []
        for x, y in points:
            dist = x**2 + y**2
            heapq.heappush(min_heap, (dist, x, y))

        heapq.heapify(min_heap)

        # pop first k points: O(klogn)
        ans = []
        while k > 0:
            __, x, y = heapq.heappop(min_heap)
            ans.append([x, y])
            k -= 1
        
        return ans