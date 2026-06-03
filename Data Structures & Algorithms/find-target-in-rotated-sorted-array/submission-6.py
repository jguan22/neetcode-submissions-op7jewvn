class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # one pass binary search
        l, r = 0, len(nums) - 1
        while l < r:
            # check which side is sorted
            mid = (l + r) // 2
            if nums[mid] >= nums[l]:     # left side is sorted
                # check if target is in the sorted range
                if nums[l] <= target <= nums[mid]:
                    r = mid
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid
        
        return l if nums[l] == target else -1

        """ # find the pivot
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        offset = l
        l, r = 0, n - 1
        while l < r:
            # convert index to offset index
            mid = (l + r) // 2
            real_mid = (mid + offset) % n
            if nums[real_mid] < target:
                l = mid + 1
            else:
                r = mid
            
        ans = (l + offset) % n
        return ans if nums[ans] == target else -1 """