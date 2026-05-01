class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        n = len(intervals)
        left, right = newInterval[0], newInterval[1]
        
        # 1. add all intervals before target
        i = 0
        while i < n and intervals[i][1] < left:
            res.append(intervals[i])
            i += 1
        
        # 2. merge all intervals onverlapped
        while i < n and intervals[i][0] <= right:
            left = min(left, intervals[i][0])
            right = max(right, intervals[i][1])
            i += 1
        res.append([left, right])

        # 3. add the rest
        res.extend(intervals[i:])
        return res