class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        ans = []
        left = newInterval[0]
        right = newInterval[1]

        i = 0
        while i < n:
            inter = intervals[i]
            # no overlapping
            if inter[1] < left:
                ans.append(inter)
            # overlapping
            elif inter[0] <= right:
                left = min(left, inter[0])
                right = max(right, inter[1])
            # overlapping stops
            else:
                break
            
            i += 1
        
        # add the new interval and loop the rest if any
        ans.append([left, right])
        while i < n:
            ans.append(intervals[i])
            i += 1

        return ans