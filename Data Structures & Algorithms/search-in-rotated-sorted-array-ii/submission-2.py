class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        l, r = 0, n-1
        while l < r:
            mid = (l + r) // 2

            # cant tell which side is sorted, so squeeze the range
            if nums[mid] == nums[l] == nums[r]:
                l += 1
                r -= 1
                continue
            
            if nums[mid] >= nums[l]:    # left side is sorted
                if nums[l] <= target <= nums[mid]:
                    r = mid
                else:
                    l = mid + 1
            
            else:   # right side is sorted
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid
        
        return nums[l] == target