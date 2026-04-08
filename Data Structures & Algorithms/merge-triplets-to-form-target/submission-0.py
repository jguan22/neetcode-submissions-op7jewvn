class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        match = [False] * 3

        for triplet in triplets:
            # skip if any number is larger than target
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue
            
            for i in range(3):
                if triplet[i] == target[i]:
                    match[i] = True
        
        return match == [True, True, True]