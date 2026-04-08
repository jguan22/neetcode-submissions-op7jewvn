class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        self.xor_total = 0

        # backtracking
        def backtrack(i, curr_total):
            # base case:
            if i >= n:
                self.xor_total += curr_total
                return
            
            # either choose this num or skip it
            backtrack(i+1, curr_total)

            curr_total ^= nums[i]
            backtrack(i+1, curr_total)
        
        backtrack(0, 0)
        return self.xor_total