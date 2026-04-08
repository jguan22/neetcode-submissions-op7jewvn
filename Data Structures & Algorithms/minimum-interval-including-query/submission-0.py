class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # sort the query based on its value
        new_quer = sorted([(q, i) for i, q in enumerate(queries)])
        ans = [0] * len(queries)

        # build a min heap with left bound lower than curr query
        # sort the interval by left bound
        intervals.sort(key=lambda x: x[0])
        min_heap = []
        
        j = 0
        n = len(intervals)
        for i in range(len(new_quer)):
            query, index = new_quer[i]

            # check if interval covers curr query
            # since query is sorted, any left is less than query will always on the left
            # only need to check right bound later
            while j < n and intervals[j][0] <= query:
                heapq.heappush(min_heap, (intervals[j][1]-intervals[j][0]+1, intervals[j][1]))
                j += 1
            
            # check the right bound
            while min_heap and min_heap[0][1] < query:
                heapq.heappop(min_heap)
            
            if not min_heap:
                ans[index] = -1
            else:
                ans[index] = min_heap[0][0]
        
        return ans