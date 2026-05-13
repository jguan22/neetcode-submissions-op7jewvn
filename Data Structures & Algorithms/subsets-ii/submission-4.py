class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # backtrack
        n = len(nums)
        nums.sort()
        ans = []
        curr_list = []

        def backtrack(start):
            # base case
            if start >= n:
                ans.append(curr_list[:])
                return
            
            # option 1: include curr num
            curr_list.append(nums[start])
            backtrack(start + 1)

            # backtrack
            curr_list.pop()

            # option 2: skip curr num and all duplicates
            while start + 1 < n and nums[start+1] == nums[start]:
                start += 1
            backtrack(start + 1)
        
        backtrack(0)
        return ans