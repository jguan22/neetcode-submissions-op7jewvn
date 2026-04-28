class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # iterate backwards from the very end: burst the last balloon
        # thus, its neighbors can be determined for every step
        new_list = [1] + nums + [1]     # add dummy at both ends for easy compute
        n = len(nums)

        # dp[i][j] is the max coins from range i to j
        dp = [[0] * (n+2) for _ in range(n+2)]
        for l in range(n, 0, -1):
            for r in range(l, n+1):
                for i in range(l, r+1):
                    # i is the last balloon, so left is l-1 and right is r+1
                    curr_gain = new_list[l-1] * new_list[i] * new_list[r+1]
                    dp[l][r] = max(dp[l][r], curr_gain + dp[l][i-1] + dp[i+1][r])
        
        return dp[1][n]