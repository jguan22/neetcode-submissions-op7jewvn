class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 0+0=0, 0+1=1, 1+0=1, 1+1=10
        # use XOR to get each digit
        # use and and shift 1 bit to handle carries
        # need to add a mask for python as no 32-bit limit
        mask = 0xFFFFFFFF
        
        while (b & mask) > 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask

        # If 'a' exceeds the maximum positive 32-bit signed int (0x7FFFFFFF)
        # it means the result is negative in 32-bit land.
        return a if a <= 0x7FFFFFFF else ~(a ^ mask)
            