"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # check the max overlap at the same time
        # compute the overlap range and pop interval with lower right bound (min heap)
        intervals.sort(key=lambda x: x.start)   # O(nlogn)
        min_heap = []
        room_needed = 0
        for interval in intervals:  # O(nlogn)
            # pop any interval that not overlap with curr one
            while min_heap and min_heap[0] <= interval.start:
                heapq.heappop(min_heap)
            
            # insert curr interval and update room needed
            heapq.heappush(min_heap, interval.end)
            room_needed = max(room_needed, len(min_heap))

        return room_needed
