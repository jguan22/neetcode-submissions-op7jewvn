class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        subset = []
        ans = []

        def backtrack(index):
            if index >= n:
                ans.append(subset[:])
                return
            
            # either include curr num
            subset.append(nums[index])
            backtrack(index+1)

            # or skip it
            subset.pop()

            # if skip, skip all duplicates
            while index+1 < n and nums[index] == nums[index + 1]:
                index += 1
            backtrack(index+1)
        

        backtrack(0)
        return ans