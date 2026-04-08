class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # prefix sum
        prefix_sum = {0: 1}
        curr_sum = 0
        ans = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            diff = curr_sum - k
            if diff in prefix_sum:
                ans += prefix_sum[diff]
            
            prefix_sum[curr_sum] = prefix_sum.get(curr_sum, 0) + 1

        return ans