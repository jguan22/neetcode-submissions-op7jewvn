class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # use a dict to track rightmost pos of each char: O(n)
        char_map = defaultdict(int)
        for i, c in enumerate(s):
            char_map[c] = i

        # update right bound of each partition until it meets curr right bound to be one partition
        # linear scan: O(n)
        partitions = []
        l, r = 0, 0
        for i, c in enumerate(s):
            r = max(r, char_map[c])

            if i == r:
                partitions.append(r - l + 1)
                l = r + 1
        
        return partitions