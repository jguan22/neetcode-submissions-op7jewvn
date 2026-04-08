class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # two pointers doesn't work well for negative numbers
        # use prefix sum: 
        prefix_sum = defaultdict(int)

        # add this case for subarray starting from 0
        prefix_sum[0] = 1
        
        ans = 0
        total_sum = 0
        for num in nums:
            total_sum += num
            diff = total_sum - k
            ans += prefix_sum[diff]
            prefix_sum[total_sum] += 1
        
        return ans