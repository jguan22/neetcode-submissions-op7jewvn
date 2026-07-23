class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # loop through intervals: O(n)
        i = 0
        n = len(intervals)
        left, right = newInterval
        res = []
        
        # 1. add all intervals on the left
        while i < n:
            if intervals[i][1] >= left:
                break
            res.append(intervals[i])
            i += 1
        
        # 2. merge overlapped intervals
        while i < n:
            if intervals[i][0] > right:
                break

            left = min(left, intervals[i][0])
            right = max(right, intervals[i][1])
            i += 1
        res.append([left, right])

        # 3. append rest of the list if any
        res.extend(intervals[i:])
        return res