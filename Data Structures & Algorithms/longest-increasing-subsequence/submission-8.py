class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # use mono stack to keep increasing order: O(nlogn)
        stack = []

        for num in nums:
            # find a bigger num
            if not stack or num > stack[-1]:
                stack.append(num)
                continue
            
            # or find the right spot for curr num
            l, r = 0, len(stack) - 1
            while l < r:
                mid = (l + r) // 2
                if num > stack[mid]:
                    l = mid + 1
                else:
                    r = mid
            
            stack[l] = num
        
        return len(stack)