class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        unique = set(nums)

        for num in unique:
            if num - 1 in unique:
                continue
            
            curr = num
            while curr + 1 in unique:
                curr += 1
            
            max_len = max(max_len, curr - num + 1)
        
        return max_len