class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        n = len(nums) - 1

        def backtrack(index, curr_list):
            # base case
            if index > n:
                # add curr list as one subset
                ans.append(curr_list.copy())
                return
            
            # either include this number
            curr_num = nums[index]
            curr_list.append(curr_num)
            backtrack(index + 1, curr_list)

            # or not include this number
            curr_list.pop()
            while index <= n and nums[index] == curr_num:
                index += 1
            backtrack(index, curr_list)
            
        
        backtrack(0, [])
        return ans