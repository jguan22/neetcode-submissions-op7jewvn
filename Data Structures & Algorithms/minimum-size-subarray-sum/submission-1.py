class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        shortest = float('inf')
        l = 0

        total = 0
        for r in range(n):
            total += nums[r]

            # adjust the left bound
            while total >= target:
                shortest = min(shortest, (r-l+1))
                total -= nums[l]
                l += 1
        
        return shortest if shortest < float('inf') else 0