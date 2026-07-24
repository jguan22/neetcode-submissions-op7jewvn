class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # create a dict to mark the far right position of each char
        far_right = defaultdict(int)
        for i, c in enumerate(s):
            far_right[c] = i

        # loop through and update the right bound
        partition = []
        left = right = 0
        for i, c in enumerate(s):
            right = max(right, far_right[c])
            
            # find the right bound of curr partition
            if i == right:
                partition.append(right - left + 1)
                left = i + 1
        
        return partition
