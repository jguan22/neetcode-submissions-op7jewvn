class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # to avoid O(n^3), sort the list and use two pointers: O(nlogn)
        nums.sort()
        n = len(nums)

        # mark one num and use two pointers to loop through the rest: O(n^2)
        ans = []
        for i in range(n-2):
            # early break
            if nums[i] > 0:
                break

            # skip duplicate
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l, r = i+1, n-1
            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]
                if curr_sum > 0:
                    r -= 1
                elif curr_sum < 0:
                    l += 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    # skip duplicate
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1

        return ans