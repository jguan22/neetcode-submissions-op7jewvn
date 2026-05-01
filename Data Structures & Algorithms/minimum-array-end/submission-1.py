class Solution:
    def minEnd(self, n: int, x: int) -> int:
        # the num in array must have 1 at each digit with 1 in x, the rest of digits can be either 1 or 0
        # thus, keep all 1 as it is, add (n-1) in 0 digit
        n -= 1  # the first num in array is x itself
        ans = x
        x_mask = 1    # start from right most digit
        n_mask = 1

        while n >= n_mask:
            # look for every 0 in x
            if (x & x_mask) == 0:
                # ans is the (n-1)th num, which is digit of (n-1) in all 0 digits in x
                if n & n_mask:
                    ans |= x_mask
                n_mask <<= 1
            
            x_mask <<= 1
            
        return ans