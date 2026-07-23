class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the intervals by left: O(nlogn)
        intervals.sort()
        left, right = intervals[0]
        res = []
        # loop through the list: O(n)
        for i in range(1, len(intervals)):
            # case 1: no overlap
            if intervals[i][0] > right:
                res.append([left, right])
                left, right = intervals[i]
                continue
            else:   # case 2: overlapped, merge them
                right = max(right, intervals[i][1])
        
        res.append([left, right])
        return res
