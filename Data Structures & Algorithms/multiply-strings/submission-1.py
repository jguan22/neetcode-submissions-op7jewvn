class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # edge case
        if num1 == '0' or num2 == '0':
            return '0'
        
        # loop through the string from low digit: O(m * n)
        num1 = num1[::-1]
        num2 = num2[::-1]

        res = [0] * (len(num1) + len(num2))
        for i in range(len(num1)):
            for j in range(len(num2)):
                num = int(num1[i]) * int(num2[j])

                # num goes to i+j and i+j+1 if any carry
                res[i+j] += num
                res[i+j+1] += (res[i+j] // 10)
                res[i+j] %= 10
        
        # skip leading zeros
        if res[-1] == 0:
            res = res[:-1]

        # turn the result back to string
        res = res[::-1]
        res = map(str, res)
        
        return "".join(res)