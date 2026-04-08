class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # use a stack to track the temp (temp, i)
        # keep stack decreasing
        # use index to compute the ans
        stack = []
        ans = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            # if temp is higher than any day before
            while stack and temp > stack[-1][0]:
                pre = stack.pop()
                ans[pre[1]] = i - pre[1]
            
            # insert into stack
            stack.append((temp, i))
        
        return ans