class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        unique = set(nums)
        seen = set()

        for num in nums:
            if num in seen:
                continue
            
            curr_len = 1
            while num + curr_len in unique:
                seen.add(num + curr_len)
                curr_len += 1

            max_len = max(max_len, curr_len)

        return max_len