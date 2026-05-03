class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # sliding window will not work since nums contain negative
        # prefix sum for a constant query
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1   # base case

        curr_sum = 0
        count = 0
        for num in nums:
            # see how many sub with (curr-k) exists, where curr - pre = k   
            curr_sum += num
            count += prefix_sum[curr_sum - k]

            # update curr to dict later to avoid count itself (k = 0 case)
            prefix_sum[curr_sum] += 1

        return count