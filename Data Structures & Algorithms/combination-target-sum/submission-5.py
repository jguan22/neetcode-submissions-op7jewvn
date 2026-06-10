class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # sort the list to easier later query
        nums.sort()
        n = len(nums)
        curr_combi = []
        combinations = []

        def backtrack(start, curr_sum):
            # base case
            if curr_sum == target:
                combinations.append(curr_combi[:])
                return
            
            for i in range(start, n):
                if curr_sum + nums[i] > target:
                    break
                
                curr_combi.append(nums[i])
                backtrack(i, curr_sum + nums[i])

                curr_combi.pop()

        backtrack(0, 0)
        return combinations