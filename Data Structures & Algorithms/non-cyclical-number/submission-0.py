class Solution:
    def isHappy(self, n: int) -> bool:
        total = 0

        while n > 0:
            digit = n % 10
            n = n // 10

            total += (digit * digit)
        
        if total // 10 > 0:
            return self.isHappy(total)
        
        return total == 1