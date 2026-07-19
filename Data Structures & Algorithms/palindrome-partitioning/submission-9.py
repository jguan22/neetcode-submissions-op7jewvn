class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # precompute all palindromes for fast query: O(n^2)
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    # single or double chars
                    if j <= i+1:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
        
        # backtracking 2^n states: O(n * 2^n)
        res = []
        curr = []

        def backtrack(start):
            if start == n:
                res.append(curr[:])
                return
            
            for end in range(start, n):
                # find a panlindrome, try this path
                if dp[start][end]:
                    curr.append(s[start:end+1])
                    backtrack(end+1)
                    curr.pop()
        
        backtrack(0)
        return res
                