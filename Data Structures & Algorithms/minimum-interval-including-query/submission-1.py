class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # sort the querries for a linear scan
        # keep track on length, right_bound of intervals using min_heap
        min_heap = []
        querry_list = [(n, i) for i, n in enumerate(queries)]
        querry_list.sort()
        n = len(queries)

        ans = [-1] * n
        intervals.sort()
        j = 0

        for i in range(n):
            curr, index = querry_list[i]
            # add intervals containing curr_num
            while j < len(intervals) and curr >= intervals[j][0]:
                # (length, right_bound)
                length = intervals[j][1] - intervals[j][0] + 1
                heapq.heappush(min_heap, (length, intervals[j][1]))
                j += 1
            
            while min_heap:
                # pop any interval doesn't contain curr anymore
                if min_heap[0][1] < curr:
                    heapq.heappop(min_heap)
                else:
                    ans[index] = min_heap[0][0]
                    break
            
        return ans