class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = []

        def backtrack(left, right):
            if left == n and right == n:
                res.append("".join(curr))
                return
            
            if left < n:
                curr.append('(')
                backtrack(left+1, right)
                curr.pop()
            
            if right < left:
                curr.append(')')
                backtrack(left, right+1)
                curr.pop()

        backtrack(0, 0)
        return res