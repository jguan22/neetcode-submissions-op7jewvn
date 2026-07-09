class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # loop through the interval list: O(n)
        n = len(intervals)
        new_list = []
        i = 0
        
        # find the position where new inverval should be
        # add intervals on the left to the list
        l, r = newInterval
        while i < n and intervals[i][1] < l:
            i += 1
        new_list.extend(intervals[:i])
        
        # merge all overlapped intervals and add the new one to the list
        if i < n:
            l = min(intervals[i][0], l)

        while i < n and intervals[i][0] <= r:
            r = max(intervals[i][1], r)
            i += 1
            
        new_list.append([l, r])

        # add intervals on the right to the list
        new_list.extend(intervals[i:])
        
        return new_list