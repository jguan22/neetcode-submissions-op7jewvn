class Solution:
    def hammingWeight(self, n: int) -> int:
        mask = 1
        total = 0
        while n > 0:
            if n & mask == 1:
                total += 1
            n >>= 1
        
        return total