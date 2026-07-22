class Solution:
    def rob(self, nums: List[int]) -> int:
        # edge case: less than 3 houses, can only rob one
        if len(nums) <= 3:
            return max(nums)

        # two cases: either rob house 1 or house n-1
        # helper to run dp twice: O(n)
        def robHouse(houses):
            n = len(houses)
            dp = [0] * (n+1)
            dp[1] = houses[0]
            for i in range(2, n+1):
                dp[i] = max(dp[i-1], dp[i-2] + houses[i-1])
            return dp[n]
        
        m = len(nums)
        case_1 = robHouse(nums[:m-1])
        case_2 = robHouse(nums[1:])
        return max(case_1, case_2)