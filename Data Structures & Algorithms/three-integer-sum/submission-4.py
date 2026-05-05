class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n-2):
            # early break
            if nums[i] > 0:
                break

            # skip duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # use two pointers to find two nums sum up to target
            target = 0 - nums[i]
            j, k = i+1, n-1
            
            while j < k:
                curr_sum = nums[j] + nums[k]
                if curr_sum == target:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    # skip duplicate
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                elif curr_sum < target:
                    j += 1
                else:
                    k -= 1

        return res