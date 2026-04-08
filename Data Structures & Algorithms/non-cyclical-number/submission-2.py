class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def sumDigits(num):
            total_sum = 0
            while num > 0:
                digit = num % 10
                total_sum += (digit * digit)
                num = num // 10
            return total_sum
        
        while n not in seen:
            seen.add(n)
            n = sumDigits(n)
            if n == 1:
                return True
        
        return False