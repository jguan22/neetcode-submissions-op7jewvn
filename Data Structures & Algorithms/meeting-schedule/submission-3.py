"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # check if there is any overlapped
        intervals.sort(key=lambda x:x.start)    # O(nlogn)
        for i in range(1, len(intervals)):  # O(n)
            if intervals[i].start < intervals[i-1].end:
                return False

        return True