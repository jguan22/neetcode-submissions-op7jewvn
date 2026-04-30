class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 3 possible res for each digit: 0 & 0 = 0, 1 & 0 = 1, 1 & 1 = 0
        # use XOR to take care of addition
        # use AND to look for a carry if both are 1
        # need a mask to avoid overflow
        mask = 0xFFFFFFFF

        while (b & mask) > 0:
            # find the carry and shift to nxt digit
            carry = (a & b) << 1

            # sum a to b, assign carry to b for nxt round
            a ^= b
            b = carry
        
        
        return a & mask if b > 0 else a