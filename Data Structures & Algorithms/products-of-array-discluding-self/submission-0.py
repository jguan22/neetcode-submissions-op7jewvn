class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # keep tracking the number of zeros
        num_zero = 0
        zero_index = -1

        # compute the product of all numbers
        product = 1

        for i, num in enumerate(nums):
            if num == 0:
                # break the loop if zero more than 1
                if num_zero > 0:
                    num_zero += 1
                    break

                num_zero += 1
                zero_index = i
                continue
            
            # compute the product if num is not zero
            product *= num

        # if more than one zero
        if num_zero > 1:
            return [0] * len(nums)
        
        ans = [0] * len(nums)
        if num_zero == 1:
            ans[zero_index] = product
        
        if num_zero == 0:
            for i in range(len(nums)):
                ans[i] = product // nums[i]
        
        return ans
