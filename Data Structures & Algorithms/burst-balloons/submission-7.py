class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # consider the process backwards as the gain when burst ith ballon at last in a given range
        # add two dummy nums at both end to deal with edge case
        new_nums = [1] + nums + [1]
        n = len(new_nums)
        dp = [[0] * n for _ in range(n)]
        
        # n^2 states and each state has n ballons: O(n^3)
        for i in range(n-2, 0, -1): # skip those two dummy nums 
            for j in range(i, n-1):
                # loop each ballon in the range
                for k in range(i, j+1):
                    curr_gain = new_nums[i-1] * new_nums[k] * new_nums[j+1]
                    total_gain = dp[i][k-1] + curr_gain + dp[k+1][j]
                    dp[i][j] = max(dp[i][j], total_gain)
        
        return dp[1][n-2]