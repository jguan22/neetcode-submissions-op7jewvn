class Solution:
    def isHappy(self, n: int) -> bool:
        # add set to prevent endless loop
        seen = set()

        # repeat until it reaches 1 or any number in seen
        while n != 1:
            # base case
            if n in seen:
                return False
            
            seen.add(n)

            total = 0
            while n > 0:
                digit = n % 10
                n //= 10
                total += digit * digit
            
            n = total
        
        return True