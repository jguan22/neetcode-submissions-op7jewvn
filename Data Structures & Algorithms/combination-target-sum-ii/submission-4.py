class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # backtracking 2^N states: O(n * 2^n)
        candidates.sort()   # O(nlogn)
        n = len(candidates)
        res = []
        curr = []

        def backtrack(start, curr_sum):
            # base case
            if curr_sum == target:
                res.append(curr[:])     # O(n)
                return

            for i in range(start, n):
                if curr_sum + candidates[i] > target:
                    break

                # skip duplicates when last same num is skipped
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                curr.append(candidates[i])
                backtrack(i+1, curr_sum + candidates[i])
                curr.pop()
        
        backtrack(0, 0)
        return res
