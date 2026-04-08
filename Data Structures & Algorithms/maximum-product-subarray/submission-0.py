class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # negative num can be max after an another negative num
        # need to keep track on max and neg
        # reset after 0
        n = len(nums)
        dp_max = [0] * n
        dp_min = [0] * n

        dp_max[0] = dp_min[0] = nums[0]

        for i in range(1, n):
            # the max either be curr num * last max, or curr num * last min, or curr num
            dp_max[i] = max(nums[i], dp_max[i-1] * nums[i], dp_min[i-1] * nums[i])

            dp_min[i] = min(nums[i], dp_max[i-1] * nums[i], dp_min[i-1] * nums[i])

        return max(dp_max)