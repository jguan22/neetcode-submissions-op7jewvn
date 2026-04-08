class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()
        curr_combi = []

        def dfs(start, curr_sum):
            if curr_sum == target:
                ans.append(curr_combi[:])
                return
            
            for i in range(start, n):
                if curr_sum + nums[i] > target:
                    break

                curr_combi.append(nums[i])
                dfs(i, curr_sum + nums[i])
                curr_combi.pop()
        
        dfs(0, 0)
        return ans