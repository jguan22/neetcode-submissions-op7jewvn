class Solution:
    def minEnd(self, n: int, x: int) -> int:
        # all digits with 1s in x must be 1 in all nums, digits 0s can be either 0 or 1
        # meaning we count the digit 0s until n nums in the list, which equals to place digits of n in x to count as n-th num
        n -= 1  # first num in the list is x itself
        ans = x
        x_mask = n_mask = 1

        # loop until all digits of n is placed in the num
        while n >= n_mask:
            if (x & x_mask) == 0:   # find a 0 to place num
                if n & n_mask:      # fill the digit with 1 if curr digit of n is 1
                    ans |= x_mask
                n_mask <<= 1
        
            x_mask <<= 1
        
        return ans