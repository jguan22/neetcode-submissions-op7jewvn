class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        stack = [nums[0]]
        for num in nums[1:]:
            if num > stack[-1]:
                stack.append(num)
            else:
                i = 0
                while stack[i] < num:
                    i += 1
                stack[i] = num
        
        return len(stack)