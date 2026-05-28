class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # do a linear scan to find the most right position of each char
        most_right = {}
        for i, c in enumerate(s):
            most_right[c] = i
        
        # second linear scan to find partitions
        partitions = []
        l, r = 0, 0
        for i, c in enumerate(s):
            # check how far curr partition needs to extend
            r = max(r, most_right[c])

            # find right bound
            if r == i:
                partitions.append(r - l + 1)
                l = r + 1
        
        return partitions