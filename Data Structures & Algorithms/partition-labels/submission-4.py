class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # find the last index of each letter
        last_index = {}
        for i, c in enumerate(s):
            last_index[c] = i

        labels = []
        l, r = 0, 0
        for i, c in enumerate(s):
            # extend the right bound
            r = max(last_index[c], r)

            # find a partition when i is curr right bound
            if r == i:
                labels.append(r - l + 1)
                l = i + 1
                
        return labels