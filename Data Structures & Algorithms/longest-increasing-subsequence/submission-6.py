from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # build a stack with stricly increasing order
        stack = []

        # find the appropriate place in stack for curr num
        for num in nums:
            if not stack or stack[-1] < num:
                stack.append(num)
            else:
                # binary search to find the smallest element >= num
                # and overwrite it to maintain the optimal sub-sequence framework
                i = bisect_left(stack, num)
                stack[i] = num
        
        return len(stack)