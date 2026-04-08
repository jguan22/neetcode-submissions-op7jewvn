class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # simplify the method to run only one binary search
        # pick a pivot to split array into two, which must be at least one sorted array.
        # find that sorted array and analyze based on this fact
        l, r = 0, len(nums)-1

        while l < r:
            # first determine which side is sorted
            mid = l + (r-l) // 2
            
            # left side is sorted
            if nums[mid] >= nums[l]:
                # see if target is in the range of left side
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
        
        return l if nums[l] == target else -1