class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        res = []

        def backtrack(start, currSum, path):
            # base case
            if currSum == target:
                res.append(path.copy())
                return
            
            for i in range(start, n):
                if currSum + candidates[i] > target:
                    return
                
                # skip duplicate
                if i > start and candidates[i] == candidates[i-1]:
                    continue
            
                # either include or skip this num
                path.append(candidates[i])
                backtrack(i+1, currSum + candidates[i], path)
                path.pop()
        
        backtrack(0, 0, [])
        return res