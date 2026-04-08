class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # use a stack to track the temp
        stack = []
        ans = [0] * len(temperatures)

        for i in range(len(temperatures)):
            # if temp is higher than any day before
            while stack and temperatures[i] > temperatures[stack[-1]]:
                pre = stack.pop()
                ans[pre] = i - pre
            
            # insert into stack
            stack.append(i)
        
        return ans