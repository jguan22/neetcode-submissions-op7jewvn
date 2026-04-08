class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the list to ensure left bound is sorted
        intervals.sort()
        n = len(intervals)
        ans = []

        i = 1
        pre = intervals[0]
        while i < n:
            curr = intervals[i]

            # no overlapping
            if curr[0] > pre[1]:
                ans.append(pre)
                pre = curr
            # overlapping
            else:
                pre[1] = max(curr[1], pre[1])
            
            i += 1
        
        ans.append(pre)
        return ans