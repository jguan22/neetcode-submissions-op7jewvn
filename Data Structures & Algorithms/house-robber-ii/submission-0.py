class Solution:
    def rob(self, nums: List[int]) -> int:
        # the first house and the last one is connected, so only one can be chosen
        # meaning either max from nums[:n] or nums[1:]
        n = len(nums)
        if n < 3:
            return max(nums)

        nums1 = nums[:n]
        nums2 = nums[1:]
        dp1 = [0] * (n-1)
        dp2 = [0] * (n-1)
        dp1[0] = nums1[0]
        dp1[1] = max(nums1[0], nums1[1])
        dp2[0] = nums2[0]
        dp2[1] = max(nums2[0], nums2[1])

        for i in range(2, n-1):
            # either rob current one or skip
            dp1[i] = max(dp1[i-2] + nums1[i], dp1[i-1])
            dp2[i] = max(dp2[i-2] + nums2[i], dp2[i-1])

        max_1 = max(dp1[n-2], dp1[n-3])
        max_2 = max(dp2[n-2], dp2[n-3])
        return max(max_1, max_2)