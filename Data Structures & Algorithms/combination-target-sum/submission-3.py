class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        combinations = []

        def backtrack(start, curr_list, curr_sum):
            if curr_sum == target:
                combinations.append(curr_list[:])
                return
            
            for i in range(start, n):
                # break early
                if curr_sum + nums[i] > target:
                    break
                
                curr_list.append(nums[i])

                # skip duplicates by incrementing start index, so it never goes backwards
                backtrack(i, curr_list, curr_sum + nums[i])
                curr_list.pop()
        

        backtrack(0, [], 0)
        return combinations