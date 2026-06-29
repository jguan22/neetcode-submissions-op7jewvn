class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # convert it to a subset problem: find the subset sumed to target (total/2) as close as possible
        total_sum = sum(stones)
        target = total_sum // 2

        dp = [False] * (target + 1)
        dp[0] = True    # base case
        
        # O(N*S)
        for stone in stones:
            for i in range(target, stone - 1, -1):
                dp[i] |= dp[i-stone]
        
        # find the closest True subset sum O(S)
        for i in range(target, -1, -1):
            if dp[i]:
                # pos + neg = total_sum; neg = i; pos = total_sum - i
                # pos - neg = total_sum - 2 * i
                return total_sum - 2 * i
                
        return -1