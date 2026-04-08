class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # no need to binary search, since need to merge anyway O(n)
        n = len(intervals)
        left_bound, right_bound = newInterval[0], newInterval[1]
        new_list = []
        rest_index = -1
        for i in range(n):
            # skip any intervals before new one
            if intervals[i][1] < left_bound:
                new_list.append(intervals[i])
            elif intervals[i][0] > right_bound: # break early
                rest_index = i
                break
            else:
                left_bound = min(left_bound, intervals[i][0])
                right_bound = max(right_bound, intervals[i][1])
        
        new_list.append([left_bound, right_bound])
        if rest_index != -1:
            new_list.extend(intervals[rest_index:]) 
        return new_list