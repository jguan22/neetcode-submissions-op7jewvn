class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(nums) - 1
    
        def DFS(index, curr_list, curr_sum):
            # return once find a combination
            if curr_sum == target:
                ans.append(curr_list.copy())
                return
            
            # return if nothing to try
            if index > n or curr_sum > target:
                return
            
            # either try adding itself or start to add others
            curr_list.append(nums[index])
            DFS(index, curr_list, curr_sum + nums[index])

            # pop curr number before move on
            curr_list.pop()
            DFS(index + 1, curr_list, curr_sum)
        
        # start from top of the list
        DFS(0, [], 0)
        return ans