class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # loop through the list, mark the num equals val
        # swap it to the back
        n = len(nums)
        ans = 0
        i, j = 0, n-1
        while i <= j:
            if nums[i] != val:
                ans += 1
                i += 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
        
        return ans