class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # precompute all palindrome as a dp problem
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n-1, -1 , -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if j - i <= 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
        
        # do normal backtrack with O(1) palindrome check
        ans = []
        def backtrack(start, curr_list):
            if start >= n:
                ans.append(curr_list[:])
                return
            
            for end in range(start, n):
                if dp[start][end]:
                    curr_list.append(s[start:end+1])
                    backtrack(end+1, curr_list)
                    curr_list.pop()
        
        backtrack(0, [])
        return ans