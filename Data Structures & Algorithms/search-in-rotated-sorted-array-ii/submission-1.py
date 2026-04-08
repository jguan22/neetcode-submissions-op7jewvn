class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # need to do linear scan if left and right end equals to mid
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            mid = (l + r) // 2
            if nums[l] == nums[mid] == nums[r]: # can't tell which side is sorted
                l += 1
                r -= 1
                continue

            if nums[mid] >= nums[l]: # left side is sorted
                if nums[l] <= target <= nums[mid]:
                    r = mid
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid

        return nums[l] == target