class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # keep both queries and intervals sorted, only add intervals into heap as left <= query
        n = len(queries)
        sorted_q = [(queries[i], i) for i in range(n)]
        sorted_q.sort()
        intervals.sort()

        # use min_heap to store (size, right), check right bound to see if query is included
        min_heap = []
        ans = [-1] * n
        j = 0
        for q, index_q in sorted_q:
            # step 1: add intervals with smaller left than query
            while j < len(intervals) and intervals[j][0] <= q:
                heapq.heappush(min_heap, ((intervals[j][1] - intervals[j][0] + 1), intervals[j][1]))
                j += 1
            
            # step 2: pop any interval on the top with right < query
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)
            
            # step 3: pick the interval with the smallest size
            ans[index_q] = min_heap[0][0] if min_heap else -1
        
        return ans