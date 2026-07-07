class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # look for the common prefix
        digits = 0
        while left != right:
            # move to higher digit until common prefix is found
            left >>= 1
            right >>= 1
            digits += 1
        
        return left << digits