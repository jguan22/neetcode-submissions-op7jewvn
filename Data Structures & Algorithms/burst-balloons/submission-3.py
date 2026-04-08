class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # build the dp table backwards from last burst to the first
        # max from (left, right) range: burst i-th balloon and do (left, i-1) and (i+1, right)
        # i-th burst = l-1 * curr_balloon * r+1
        n = len(nums)
        dp = [[0] * (n+2) for _ in range(n+2)]
        new_nums = [1] + nums + [1]

        for l in range(n, 0, -1):
            for r in range(l, n+1):
                for i in range(l, r+1):
                    curr = new_nums[l-1] * new_nums[i] * new_nums[r+1]
                    dp[l][r] = max(dp[l][r], dp[l][i-1] + curr + dp[i+1][r])
        
        return dp[1][n]