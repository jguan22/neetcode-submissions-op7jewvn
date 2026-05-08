class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # one pass binary search
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2

            # special case: cant tell which side is sorted
            if nums[l] == nums[r] == nums[mid]:
                # shrink the window
                l += 1
                r -= 1
                continue

            # check which side is sorted
            if nums[mid] >= nums[l]:
                if nums[l] <= target <= nums[mid]:
                    r = mid
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid
        
        return True if nums[l] == target else False