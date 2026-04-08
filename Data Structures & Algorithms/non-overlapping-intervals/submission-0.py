class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        n = len(intervals)
        count = 0

        i = 1
        pre = intervals[0]
        while i < n:
            curr = intervals[i]

            # no overlapping
            if pre[1] <= curr[0]:
                pre = curr
            else:
                # overlapping
                # keep the one with less right
                pre[1] = min(pre[1], curr[1])
                count += 1

            i += 1
        
        return count