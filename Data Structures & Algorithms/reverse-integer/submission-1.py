class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        sign = 1
        if x < 0:
            x = -x
            sign = -1
        
        max = 2**31 - 1
        while x > 0:
            ans *= 10
            ans += x % 10
            x = x // 10
            if ans > max:
                return 0
            
        return ans*sign