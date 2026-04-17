class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        combinations = []

        def backtrack(start, curr_list, curr_sum):
            if curr_sum == target:
                combinations.append(curr_list[:])
                return
            
            for i in range(start, n):
                # skip duplicates
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                    
                if curr_sum + candidates[i] > target:
                    break
                
                curr_list.append(candidates[i])
                backtrack(i+1, curr_list, curr_sum + candidates[i])
                curr_list.pop()
        
        backtrack(0, [], 0)
        return combinations