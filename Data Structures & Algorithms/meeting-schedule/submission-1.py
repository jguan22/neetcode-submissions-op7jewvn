"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # look for any overlap
        intervals.sort(key=lambda x: x.start)
        pre_right = float('-inf')
        for i in range(len(intervals)):
            if intervals[i].start < pre_right:
                return False
            else:
                pre_right = intervals[i].end
        
        return True