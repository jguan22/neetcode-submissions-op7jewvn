class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []

        def backtrack(index, currSum, path):
            # base case
            if currSum == target:
                res.append(path.copy())
            
            # explore the list
            for i in range(index, n):
                # once sum is too large, skip rest of the list
                if currSum + nums[i] > target:
                    return

                path.append(nums[i])
                backtrack(i, currSum + nums[i], path)
                path.pop()
        
        backtrack(0, 0, [])
        return res