class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # one only exist in the common prefix
        # we can check left and right most num and find out prefix
        i = 0
        while left != right:
            left >>= 1
            right >>= 1
            i += 1
        return left << i