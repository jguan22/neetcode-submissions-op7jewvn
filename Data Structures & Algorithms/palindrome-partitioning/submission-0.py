class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        n = len(s)


        def backtrack(index, curr_list):
            # base case: successfully reach the end, a valid case
            if index >= n:
                ans.append(curr_list.copy())
                return

            for end in range(index + 1, n + 1):
                # check if current substring is palindrome
                substring = s[index:end]
                if is_palindrome(substring):
                    curr_list.append(substring)
                    backtrack(end, curr_list)
                    curr_list.pop()

        def is_palindrome(sub):
            return sub == sub[::-1]

        backtrack(0, [])
        return ans