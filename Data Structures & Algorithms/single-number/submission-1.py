class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # use bit XOR
        ans = 0
        for num in nums:
            ans ^= num
        return ans