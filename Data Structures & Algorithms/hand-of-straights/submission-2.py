class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        freq_map = Counter(hand)
        unique = sorted(freq_map.keys())
        for num in unique:
            freq = freq_map[num]
            if freq == 0:
                continue

            for i in range(groupSize):
                curr = num + i
                if freq_map[curr] < freq:
                    return False
                freq_map[curr] -= freq
        
        return True