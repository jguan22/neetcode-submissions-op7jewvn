class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # find each num one by one and check if other digits are higher
        match = [False] * 3
        for trip in triplets:
            # skip if any digits are larger than target
            if trip[0] > target[0] or trip[1] > target[1] or trip[2] > target[2]:
                continue
            for i in range(3):
                if trip[i] == target[i]:
                    match[i] = True
        return match == [True] * 3