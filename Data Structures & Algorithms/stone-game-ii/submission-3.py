class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # dfs with memo
        n = len(piles)
        memo = {}

        # precompute suffix sum: O(n)
        suffix_sum = [0] * (n + 1)
        for i in range(n-1, -1, -1):
            suffix_sum[i] = suffix_sum[i+1] + piles[i]

        # dfs helper: n position(start), each has n states(M)
        # in each dfs function, need to loop through n times(X)
        # so total runtime: O(n^3)
        def dfs(start, M):
            # base case: take all stone if possible
            if start + 2*M >= n:
                return suffix_sum[start]
            
            if (start, M) in memo:
                return memo[(start, M)]
            
            # try all combinations to find the max take O(n)
            max_take = 0
            for X in range(1, 2*M + 1):
                # take X and opponent's turn starting from (start + X)
                curr_take = suffix_sum[start] - dfs(start + X, max(M, X))
                max_take = max(max_take, curr_take)
            
            memo[(start, M)] = max_take
            return max_take
        

        return dfs(0, 1)