class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates) - 1
        candidates.sort()

        def DFS(index, curr_list, curr_sum):
            if curr_sum == target:
                ans.append(curr_list.copy())
                return
            
            if index > n or curr_sum > target:
                return
            
            curr_num = candidates[index]

            # either include itself or not include itself
            curr_list.append(curr_num)
            DFS(index + 1, curr_list, curr_sum + curr_num)

            curr_list.pop()
            index += 1
            # skip the duplicates to avoid same combination
            while index <= n and candidates[index] == curr_num:
                index += 1
            DFS(index, curr_list, curr_sum)

        DFS(0, [], 0)
        return ans