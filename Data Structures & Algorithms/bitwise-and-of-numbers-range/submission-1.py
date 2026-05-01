class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # bitwise AND means the same digit must all be 1 to make final digit be 1, else 0
        # thus, look for the common prefix of all num in range(everything else be 0)
        digits_zero = 0
        while left != right:
            # move one digit until prefix is found
            left >>= 1
            right >>= 1
            digits_zero += 1
        
        # return prefix and 0s on the right
        return left << digits_zero