class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # backtracking n^(target/m) states, where m is min num in the nums
        nums.sort() # O(nlogn)
        n = len(nums)
        res = []

        def backtrack(start, curr_list, curr_sum):
            # base case:
            if start > n:
                return
            
            if curr_sum == target:
                res.append(curr_list[:])
                return
            
            for i in range(start, n):
                # break early
                if curr_sum + nums[i] > target:
                    break
                
                curr_list.append(nums[i])
                backtrack(i, curr_list, curr_sum + nums[i])

                curr_list.pop()
        
        backtrack(0, [], 0)
        return res
                