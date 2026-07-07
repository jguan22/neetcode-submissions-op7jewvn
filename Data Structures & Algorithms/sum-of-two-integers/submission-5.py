class Solution:
    def getSum(self, a: int, b: int) -> int:
        # use XOR to deal with sum and AND to deal with carry
        mask = 0xFFFFFFFF
        
        # 32 bits: O(1)
        while b != 0:
            # only both digits are 1 to result in a carry on next digit
            carry = (a & b) << 1

            # curr digit is the XOR result of both num, save in a
            a ^= b

            # confine both to 32-bit unsigned integers
            a = a & mask
            b = carry & mask
        
        return a if a <= 0x7FFFFFFF else ~(a ^ mask)