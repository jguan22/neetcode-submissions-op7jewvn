class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        longest = 0

        for num in unique:
            if num - 1 in unique:
                continue
            
            current = 1
            while num + 1 in unique:
                current += 1
                num += 1
            longest = max(current, longest)
        
        return longest