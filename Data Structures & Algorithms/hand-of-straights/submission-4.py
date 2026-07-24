class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # gready: starting from the lowest num and go up by groupSize
        freq_map = Counter(hand)            # O(n)
        unique = sorted(freq_map.keys())    # O(mlogm)

        for num in unique:
            # curr num is drained, move on to the next one
            curr_freq = freq_map[num]
            if curr_freq == 0:
                continue
            
            # form groups as many as curr num
            for i in range(groupSize):
                curr = num + i
                if freq_map[curr] < curr_freq:
                    return False
                
                freq_map[curr] -= curr_freq
        
        return True