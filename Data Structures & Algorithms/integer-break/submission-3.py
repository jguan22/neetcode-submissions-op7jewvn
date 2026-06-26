class Solution:
    def integerBreak(self, n: int) -> int:
        # the max product is using as many 3 as possible
        # edge case: 2, 3
        if n < 4:
            return n - 1

        # until the remaining is less than 4: O(n)
        product = 1
        while n > 4:
            n -= 3
            product *= 3

        return product * n