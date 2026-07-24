class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # looking for at least three triplets to have all three target digits
        # and the rest of two must be lesser or equal
        matched = [False] * 3

        for tri in triplets:    # O(n)
            # skip if any num larger than target
            if tri[0] > target[0] or tri[1] > target[1] or tri[2] > target[2]:
                continue
            
            for i in range(3):
                if tri[i] == target[i]:
                    matched[i] = True
        
        return matched == [True] * 3
