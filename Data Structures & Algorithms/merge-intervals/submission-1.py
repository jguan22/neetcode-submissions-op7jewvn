class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged_list = []

        for start, end in intervals:
            if merged_list and start <= merged_list[-1][1]:
                pre_start, pre_end = merged_list.pop()
                start = pre_start
                end = max(end, pre_end)
            
            merged_list.append([start, end])

        return merged_list