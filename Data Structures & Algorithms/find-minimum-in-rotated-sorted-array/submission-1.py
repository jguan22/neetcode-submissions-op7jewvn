class Solution:
    def findMin(self, nums: List[int]) -> int:
        # target is the only num in the list that is less than its left
        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + (r-l) // 2

            # look for the first num that is less than nums[r]
            if nums[mid] < nums[r]:
                # search left
                r = mid
            else:
                l = mid + 1
        
        return nums[l]