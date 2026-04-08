class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        # starting from the lowest digits
        num1 = num1[::-1]
        num2 = num2[::-1]

        # the highest digit result can possibly have
        res = [0] * (len(num1) + len(num2))
        for i in range(len(num1)):
            for j in range(len(num2)):
                num = int(num1[i]) * int(num2[j])

                # curr num goes to digit i+j
                # carry goes to i+j+1
                # as digit only goes up when looping, we can deal with higher digit carry later
                res[i+j] += num
                res[i+j+1] += (res[i+j] // 10)
                res[i+j] %= 10
        
        if res[-1] == 0:
            res = res[:-1]

        # turn the result back to string
        res = res[::-1]
        res = map(str, res)
        
        return "".join(res)