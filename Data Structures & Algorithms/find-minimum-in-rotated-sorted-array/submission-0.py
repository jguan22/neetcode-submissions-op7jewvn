class Solution:
    def findMin(self, nums: List[int]) -> int:
        # find the position where nums[i] < nums[i-1]
        lo = 0
        hi = len(nums) - 1

        while lo < hi:
            mid = (lo + hi) // 2

            if nums[mid] <= nums[hi]:
                hi = mid
            else:
                lo = mid + 1
        
        return nums[lo]