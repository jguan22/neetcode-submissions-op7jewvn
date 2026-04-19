class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        combinations = []
        word_set = set(wordDict)

        # precompute the possible word in s
        dp = [[False] * n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i:j+1] in word_set:
                    dp[i][j] = True

        def backtrack(start, curr_list):
            if start == n:
                combinations.append(" ".join(curr_list))
                return
            
            for end in range(start, n):
                if dp[start][end]:
                    curr_list.append(s[start:end+1])
                    backtrack(end+1, curr_list)
                    curr_list.pop()


        backtrack(0, [])
        return combinations