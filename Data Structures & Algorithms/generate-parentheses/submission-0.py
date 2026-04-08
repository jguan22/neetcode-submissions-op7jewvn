class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []


        def backtrack(curr_combi, left):
            # base case
            if len(curr_combi) >= 2*n:
                ans.append(curr_combi)
                return
            
            # either add left parentheie when available
            if left < n:
                backtrack(curr_combi + "(", left + 1)

            # or add right parentheis when valid (less right than left)
            if (len(curr_combi) - left) < left:
                backtrack(curr_combi + ")", left)
            
        
        backtrack("", 0)
        return ans