class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # use a set to find all unique elements in list: O(n)
        unique = set(nums)

        # loop through the set items to find longest: O(n)
        max_len = 0
        for num in unique:
            # only start counting at the begining of a sequence
            if num - 1 in unique:
                continue
            
            curr_len = 1
            while num + 1 in unique:
                curr_len += 1
                num += 1
            
            max_len = max(max_len, curr_len)
        
        return max_len