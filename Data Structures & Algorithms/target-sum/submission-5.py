class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # split array into two: pos and neg
        # pos + neg = total and pos - neg = target, so, 2 * pos = total + target
        # convert to a subset sum problem to (total + target // 2)
        # sanity check
        total = sum(nums)
        if abs(target) > total or (total + target) % 2 != 0:
            return 0

        target2 = (total + target) // 2
        n = len(nums)
        dp = [0] * (target2 + 1)
        dp[0] = 1

        for num in nums:
            for i in range(target2, -1, -1):
                if num > i:
                    break
                
                dp[i] += dp[i - num]
        
        return dp[target2]


        ''' # dp to find all possible res to see if target is possible
        # sanity check
        offset = sum(nums)
        if abs(target) > offset:
            return 0
        
        n = len(nums)
        dp = [[0] * (2 * offset + 1) for _ in range(n)]

        # base case: first num could be 0
        dp[0][offset + nums[0]] += 1   
        dp[0][offset - nums[0]] += 1

        for i in range(1, n):
            for j in range(2 * offset + 1):
                if dp[i-1][j] > 0:
                    dp[i][j - nums[i]] += dp[i-1][j]
                    dp[i][j + nums[i]] += dp[i-1][j]
        
        return dp[n-1][target + offset] 
        '''