class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # fix two and loop other two
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # --- PRUNING ---
            # If the 4 smallest numbers are > target, no need to continue
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            # If nums[i] + 3 largest numbers are < target, skip this i
            if nums[i] + nums[n-1] + nums[n-2] + nums[n-3] < target:
                continue
                
            for j in range(i+1, n-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                
                curr_sum = nums[i] + nums[j]
                l, r = j+1, n-1
                while l < r:
                    total = curr_sum + nums[l] + nums[r]
                    if total < target:
                        l += 1
                    elif total > target:
                        r -= 1
                    else:
                        ans.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1
            
        return ans