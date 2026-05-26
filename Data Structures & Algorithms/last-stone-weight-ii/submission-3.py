class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # subset sum problem: look for a sum to target (half of total sum)
        total = sum(stones)
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True    # base case

        for stone in stones:
            for i in range(target, -1, -1):     # backwards to use each stone only once
                if stone > i:
                    break
                
                if dp[i - stone]:
                    dp[i] = True
        
        # find the largest possible subset sum
        for i in range(target, -1, -1):
            if dp[i]:
                return total - 2 * i
        
        return -1

        
        '''
        # split the pile into two subsets: look for the target subset sum
        n = len(stones)
        total_sum = sum(stones)
        target = total_sum // 2
        dp = [False] * (target + 1)
        dp[0] = True

        # see if target sum is achievable
        for stone in stones:
            for t in range(target, stone - 1, -1):
                if dp[t - stone]:
                    dp[t] = True
        
        # find the largest sum that closed to the target
        for t in range(target, -1, -1):
            if dp[t]:
                # the result is (total - target_sum) - target_sum
                return total_sum - 2*t
        
        return 0
        '''