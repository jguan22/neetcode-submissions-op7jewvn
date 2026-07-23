class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # greedy: when overlap occurs, drop the one with further right bound
        # which has higher chance to overlap with others
        intervals.sort()    # O(nlogn)
        count = 0
        right = intervals[0][1]
        for i in range(1, len(intervals)):  # O(n)
            # case 1: overlapped, drop the one with higher right
            if intervals[i][0] < right:
                count += 1
                right = min(right, intervals[i][1])
            else:
                right = intervals[i][1]
        
        return count