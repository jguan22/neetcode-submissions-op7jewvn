class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # keep track on the right bound
        # greedy: keep the one with less right
        intervals.sort()
        pre_right = intervals[0][1]
        count = 0
        for i in range(1, len(intervals)):
            curr_left, curr_right = intervals[i][0], intervals[i][1]
            if curr_left >= pre_right:
                pre_right = curr_right
                continue
            
            pre_right = min(pre_right, curr_right)
            count += 1

        return count