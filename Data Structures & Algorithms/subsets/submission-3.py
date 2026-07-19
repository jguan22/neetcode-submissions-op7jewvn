class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # backtracking 2^n states: O(n * 2^n)
        n = len(nums)
        subsets = []
        curr_set = []

        def backtrack(i):
            # base case: O(n)
            if i == n:
                subsets.append(curr_set[:])
                return
            
            # either add curr num or skip it
            curr_set.append(nums[i])
            backtrack(i+1)

            curr_set.pop()
            backtrack(i+1)
        
        backtrack(0)
        return subsets
                