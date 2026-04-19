class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        combinations = []
        word_set = set(wordDict)

        def backtrack(start, curr_list):
            if start == n:
                combinations.append(" ".join(curr_list))
                return
            
            for end in range(start+1, n+1):
                if s[start:end] in word_set:
                    curr_list.append(s[start:end])
                    backtrack(end, curr_list)
                    curr_list.pop()


        backtrack(0, [])
        return combinations