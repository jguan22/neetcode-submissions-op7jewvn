class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # consider this process backwards: every gain depends on which balloons left next to curr one
        # dp[i][j] = max gain from ith to jth range
        new_list = [1] + nums + [1]     # add dummy nums at both end
        n = len(new_list)
        dp = [[0] * n for _ in range(n)]
        
        # loop backwards to start with single balloon: O(n^3)
        for i in range(n-2, 0, -1):
            for j in range(i, n-1):
                # try each balloon in this range to find the max gain
                for k in range(i, j+1):    
                    # consider k is the last balloon to burst in this range
                    curr_gain = new_list[i-1] * new_list[k] * new_list[j+1]
                    total_gain = dp[i][k-1] + curr_gain + dp[k+1][j]
                    dp[i][j] = max(dp[i][j], total_gain)

        # return max gain excluding dummy nums
        return dp[1][n-2]