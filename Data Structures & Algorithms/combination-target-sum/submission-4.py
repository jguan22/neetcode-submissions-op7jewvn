class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # backtrack
        n = len(nums)
        nums.sort()
        curr_list = []
        ans = []

        def backtrack(start, curr_sum):
            if curr_sum == target:
                ans.append(curr_list[:])
                return
            
            for i in range(start, n):
                if curr_sum + nums[i] > target:
                    break
                
                curr_list.append(nums[i])
                backtrack(i, curr_sum + nums[i])
                curr_list.pop()
            
        backtrack(0, 0)
        return ans