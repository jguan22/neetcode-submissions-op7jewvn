class Solution:
    def countBits(self, n: int) -> List[int]:
        # everytime the bit reach a new significant bit (2^n), it repeats the previous cycle + 1 on the significant bit
        # thus, use dp to avoid repeating calculations
        dp = [0] * (n+1)
        offset = 1

        for i in range(1, n+1):
            # the new cycle begin at power of 2
            if offset * 2 == i:
                offset *= 2
            
            dp[i] = 1 + dp[i-offset]

        return dp