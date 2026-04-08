"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) <= 1:
            return True

        # detect if there is any overlapping
        intervals.sort(key=lambda i:i.start)

        pre = intervals[0].end
        for i in range(1, len(intervals)):
            if pre > intervals[i].start:
                return False
            else:
                pre = intervals[i].end
        
        return True