class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        dp = {}
        suffix_sum = [0] * (n+1)
        for i in range(n-1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]

        # helper to find the max stones one can find at start with M
        def dfs(start, M):
            if start >= n:
                return 0

            if start + 2*M >= n:
                return suffix_sum[start]
            
            if (start, M) in dp:
                return dp[(start, M)]
            
            max_stones = 0
            for X in range(1, 2 * M + 1):
                # Current player takes X
                # next player starts at start + X with new M
                opponent_best = dfs(start + X, max(M, X))
                max_stones = max(max_stones, suffix_sum[start] - opponent_best)
            
            dp[(start, M)] = max_stones
            return max_stones
            
            dp[(start, M)] = ans
            return ans
    
        return dfs(0, 1)
