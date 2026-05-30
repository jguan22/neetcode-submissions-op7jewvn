class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # use a min heap to find the smallest interval available
        min_heap = []   # (size, right)

        # sort the intervals in left bound, and sort the queries in ascending order
        # to once an interval on the left of one query, it's always on the left for the rest of list
        # then check on the right bound to include curr query
        sorted_queries = sorted([(q, i) for i, q in enumerate(queries)])
        res = [-1] * len(queries)
        n = len(intervals)
        intervals.sort()
        j = 0

        for q, i in sorted_queries:
            # 1. add intervals into heap
            while j < n and intervals[j][0] <= q:
                left, right = intervals[j]
                heapq.heappush(min_heap, (right - left + 1, right))
                j += 1
            
            # 2. pop any interval with right bound smaller than q
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)

            # 3. pick a interval with smaller size
            if min_heap:
                res[i] = min_heap[0][0]

        return res  