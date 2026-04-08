"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # edge case:
        if len(intervals) == 0:
            return 0

        # find all overlapping range
        intervals.sort(key=lambda x:x.start)
        min_heap = [intervals[0].end]

        max_count = 1
        for i in range(1, len(intervals)):
            # find overlapping
            if intervals[i].start < min_heap[0]:

                # store all right bounds in heap
                heapq.heappush(min_heap, intervals[i].end)
            else:
                max_count = max(max_count, len(min_heap))

                # pop out any interval that no longer overlap
                while min_heap and intervals[i].start >= min_heap[0]:
                    heapq.heappop(min_heap)
                
                heapq.heappush(min_heap, intervals[i].end)

        max_count = max(max_count, len(min_heap))
        return max_count