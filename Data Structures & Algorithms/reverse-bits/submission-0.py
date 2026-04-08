class Solution:
    def reverseBits(self, n: int) -> int:
        # move the bit and & it with 1 to check each digit
        # put the bit into ans starting at the begining
        ans = 0
        for i in range(32):
            bit = (n >> i) & 1
            ans |= (bit << (31 - i))
        
        return ans