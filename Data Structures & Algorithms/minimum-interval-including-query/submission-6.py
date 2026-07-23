class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # use min heap to pop the smallest one with query: O(mlogm + nlogn)
        # sort the query and intervals to manage curr range in a linear scan
        intervals.sort()    # O(mlogm)
        m = len(intervals)
        q_list = [(q, i) for i, q in enumerate(queries)]
        q_list.sort()       # O(nlogn)
        n = len(q_list)
        ans = [-1] * n
        min_heap = []       # O(mlogm)

        j = 0
        for q, i in q_list:
            # 1. add intervals with left bound smaller than q
            while j < m and intervals[j][0] <= q:
                # need to keep track on right bound as indicator to pop it out later
                l, r = intervals[j]
                heapq.heappush(min_heap, (r-l+1, r))
                j += 1
            
            # 2. pop any intervals with right bound smaller than q (no overlap)
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)
            
            # 3. top of heap is the answer if any
            if min_heap:
                ans[i] = min_heap[0][0]
        
        return ans