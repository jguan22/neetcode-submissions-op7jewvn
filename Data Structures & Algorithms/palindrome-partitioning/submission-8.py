class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # precompute possible palindrome
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    # base case: one or two char
                    if j <= i + 1:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
        
        # backtrack
        curr_list = []
        partitions = []

        def backtrack(start):
            # base case
            if start >= n:
                partitions.append(curr_list[:])
                return
            
            for end in range(start, n):
                if dp[start][end]:
                    curr_list.append(s[start:end+1])
                    backtrack(end + 1)
                    curr_list.pop()

        backtrack(0)            
        return partitions