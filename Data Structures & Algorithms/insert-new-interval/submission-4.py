class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end = newInterval
        res = []
        n = len(intervals)
        i = 0

        # add intervals before new one
        while i < n and intervals[i][1] < start:
            res.append(intervals[i])
            i += 1
        
        # merge intervals with new one if overlapped
        while i < n and intervals[i][0] <= end:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1
        res.append([start, end])

        # add the rest
        res.extend(intervals[i:])

        return res