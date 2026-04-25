class Solution:
    def integerBreak(self, n: int) -> int:
        # break the int to as much 3 as possible
        # anything bigger than 4 has less product than break it: 2 * 2 = 4
        # edge case:
        if n <= 3:
            return n - 1
        
        product = 1
        while n > 4:
            n -= 3
            product *= 3
        
        return product * n