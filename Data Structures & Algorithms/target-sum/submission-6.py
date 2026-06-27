class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # split list into two lists: one pos and one neg
        # pos + neg == target; pos - neg == total_sum
        # 2 * pos == target + total_sum
        # sanity check
        total_sum = sum(nums)
        if abs(target) > total_sum or (total_sum + target) % 2 != 0:
            return 0
        
        # convert it to a subset sum problem: O(m)
        new_target = (total_sum + target) // 2
        dp = [0] * (new_target + 1)
        dp[0] = 1   # base case

        # nested loop: O(n*m)
        for num in nums:
            for i in range(new_target, -1, -1):
                if num > i:
                    break
                
                dp[i] += dp[i - num]
        
        return dp[new_target]


        ''' # dp to find all possible res to see if target is possible
        # sanity check
        offset = sum(nums)
        if abs(target) > offset:
            return 0
        
        # O(m)
        n = len(nums)
        dp = [[0] * (2 * offset + 1) for _ in range(n)]

        # base case: first num could be 0
        dp[0][offset + nums[0]] += 1   
        dp[0][offset - nums[0]] += 1

        # O(n*m)
        for i in range(1, n):
            for j in range(2 * offset + 1):
                if dp[i-1][j] > 0:
                    dp[i][j - nums[i]] += dp[i-1][j]
                    dp[i][j + nums[i]] += dp[i-1][j]
        
        return dp[n-1][target + offset] 
        '''