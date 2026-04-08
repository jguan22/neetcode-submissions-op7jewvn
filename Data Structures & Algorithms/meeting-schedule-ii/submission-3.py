"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # find the most overlapped intervals at a time
        # need to track on the overlapped right bound
        # pop it out when not overlap with new interval
        n = len(intervals)
        intervals.sort(key=lambda x: x.start)
        max_room = 0
        curr_room = 0
        min_heap = []

        for i in range(n):
            while min_heap and intervals[i].start >= min_heap[0]:
                heapq.heappop(min_heap)
                curr_room -= 1

            heapq.heappush(min_heap, intervals[i].end)
            curr_room += 1
            
            max_room = max(max_room, curr_room)
        
        return max_room