class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # backtracking: n! states: O(n*n!)
        n = len(nums)
        used = [False] * n
        res = []
        curr = []

        def backtrack():
            # base case: O(n)
            if len(curr) == n:
                res.append(curr[:])
                return
            
            # loop through the list
            for i in range(n):
                if used[i]:
                    continue
                
                # either include or skip
                curr.append(nums[i])
                used[i] = True
                backtrack()
                curr.pop()
                used[i] = False
        
        backtrack()
        return res