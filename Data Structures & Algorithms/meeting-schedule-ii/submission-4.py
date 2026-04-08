"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = len(intervals)
        intervals.sort(key=lambda x: x.start)
        max_room = 0
        min_heap = []

        for i in range(n):
            while min_heap and intervals[i].start >= min_heap[0]:
                heapq.heappop(min_heap)

            heapq.heappush(min_heap, intervals[i].end)
            
            max_room = max(max_room, len(min_heap))
        
        return max_room