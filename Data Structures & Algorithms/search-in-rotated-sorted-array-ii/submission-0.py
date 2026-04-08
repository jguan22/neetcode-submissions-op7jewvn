class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # one pass: binary search
        l, r = 0, len(nums)-1

        while l < r:
            mid = l + (r-l) // 2

            # edge case: when we cant tell which side is sorted due to duplicates, shrink the bound by 1
            if nums[l] == nums[mid] == nums[r]:
                l += 1
                r -= 1
                continue

            # determine the sorted side
            if nums[mid] >= nums[l]:
                # left side is sorted
                if nums[l] <= target <= nums[mid]:
                    r = mid
                else:
                    l = mid + 1
            else:
                # right side is sorted
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid
        
        return True if nums[l] == target else False