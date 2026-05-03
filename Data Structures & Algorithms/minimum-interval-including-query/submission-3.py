class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # sort the queries in asending order 
        q_list = [(q, i) for i, q in enumerate(queries)]
        q_list.sort()
        ans = [-1] * len(q_list)
        
        # sort by left bound and add intervals in min heap as right bound going up to include curr query
        min_heap = []       # (size, right)
        intervals.sort()

        j = 0
        for q, i in q_list:
            # 1. add interval to heap
            while j < len(intervals) and intervals[j][0] <= q:
                left, right = intervals[j]
                heapq.heappush(min_heap, (right - left + 1, right))
                j += 1
            
            # 2. pop interval not includes q anymore
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)
            
            # 3. pick the smallest one if available
            if min_heap:
                ans[i] = min_heap[0][0]

        return ans