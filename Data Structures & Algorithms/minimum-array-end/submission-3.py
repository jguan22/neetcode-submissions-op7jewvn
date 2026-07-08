class Solution:
    def minEnd(self, n: int, x: int) -> int:
        # all digits of 1 in x must be 1, and all digits of 0 can be either 0 or 1
        # need to put total n nums in digits with 0
        # first possible int is x itself
        ans = x
        n -= 1

        # use a mask to track curr digit
        x_mask = 1

        # check all digits of n: O(logn)
        while n > 0:
            # if curr digit of x is 0
            if (x & x_mask) == 0:
                # put curr digit of n in
                if n & 1:
                    ans |= x_mask

                # move up n digit
                n >>= 1
            
            # move up x digit
            x_mask <<= 1

        return ans