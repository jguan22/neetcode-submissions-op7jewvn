class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # use prefix sum for fast query
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1

        curr_sum = 0
        count = 0

        # loop through all num: O(n)
        for num in nums:
            # update total sum until curr num
            curr_sum += num

            # check if a subarray sumed to k exists (curr - prefix = k)
            target = curr_sum - k
            if target in prefix_sum:
                count += prefix_sum[target]
            
            # update prefix sum now to avoid edge case as k = 0
            prefix_sum[curr_sum] += 1

        return count