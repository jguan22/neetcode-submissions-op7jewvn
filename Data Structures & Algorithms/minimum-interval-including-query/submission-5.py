class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # the total time complexity: O(mlogm + nlogn)
        # looking for the size of the smallest interval: use min_heap to track size
        # sort the queries and intervals by left bounds: easier to handle the range of intervals to include int
        intervals.sort()    # O(mlogm)
        sorted_queries = sorted([(q, i) for i, q in enumerate(queries)])    # O(nlogn)
        min_heap = []   # (size, right)

        # loop through queries: O(n + mlogm)
        ans = [-1] * len(queries)
        inter_i = 0
        m = len(intervals)
        for q, i in sorted_queries:
            # 1. add intervals to min heap: O(mlogm)
            while inter_i < m and intervals[inter_i][0] <= q:
                l, r = intervals[inter_i]
                heapq.heappush(min_heap, (r - l + 1, r))
                inter_i += 1
            
            # 2. pop any interval doesn't include q anymore
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)
            
            # 3. pick the smallest one if any
            if min_heap:
                ans[i] = min_heap[0][0]
        
        return ans