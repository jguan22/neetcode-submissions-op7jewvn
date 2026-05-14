class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # backtrack
        n = len(candidates)
        candidates.sort()
        ans = []
        curr_list = []

        def backtrack(start, curr_sum):
            if curr_sum == target:
                ans.append(curr_list[:])
                return
            
            for i in range(start, n):
                if curr_sum + candidates[i] > target:
                    break
                
                # skip duplicates
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                curr_list.append(candidates[i])
                backtrack(i + 1, curr_sum + candidates[i])
                curr_list.pop()

        backtrack(0, 0)
        return ans