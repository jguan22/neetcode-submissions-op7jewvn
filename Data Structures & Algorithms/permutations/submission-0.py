class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(curr_list, num_to_choose):
            # add to ans when all numbers are used
            if not num_to_choose:
                ans.append(curr_list.copy())
                return

            # fill the combination with each number in the list
            n = len(num_to_choose)
            for i in range(n):
                # fill this position and move to the next
                curr_list.append(num_to_choose[i])
                remaining_num = num_to_choose[:i] + num_to_choose[i+1:]
                backtrack(curr_list, remaining_num)

                # pop current number and use next one in the list
                curr_list.pop()
        
        num_to_choose = nums.copy()
        backtrack([], num_to_choose)
        return ans