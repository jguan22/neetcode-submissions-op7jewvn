class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # use a set to track all nums
        num_set = set(nums)

        # loop through each unique num
        max_len = 0
        for num in num_set:
            # skip if it has a num on its left
            if num - 1 in num_set:
                continue
            
            # start counting a sequence if curr num is the first one in the set
            curr = num
            while curr + 1 in num_set:
                curr += 1
            
            max_len = max(max_len, curr - num + 1)
        
        return max_len