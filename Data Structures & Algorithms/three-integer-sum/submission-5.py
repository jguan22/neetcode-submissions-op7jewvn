class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # use two pointers
        # sort the num to easier avoid duplicates: O(nlogn)
        n = len(nums)
        nums.sort()
        ans = []
        
        # loop through the list: O(n^2)
        for i in range(n):
            # skip duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            target = -nums[i]
            
            # set up two pointers to find possible combinations: O(n)
            j, k = i + 1, n - 1
            while j < k:
                curr_sum = nums[j] + nums[k]
                
                # find a triplet
                if curr_sum == target:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    # skip duplicates
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                elif curr_sum > target:
                    # need smaller sum
                    k -= 1
                else:
                    # need bigger sum
                    j += 1

        return ans   