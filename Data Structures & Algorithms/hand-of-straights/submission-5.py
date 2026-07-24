class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # gready: starting from the lowest num and go up by groupSize O(n)
        freq_map = Counter(hand)            # O(n)

        for num in hand:
            # skip if already drained or not the start of sequence
            if freq_map[num - 1] > 0 or freq_map[num] == 0:
                continue
            
            # once find the start, form groups
            # use a queue to show how many active groups at curr position
            curr = num
            queue = deque()
            active = 0
            while freq_map[curr] > 0 or active > 0:
                # group is formed, move num of active group which begins at start
                if len(queue) == groupSize:
                    active -= queue.popleft()
                
                # check curr num if it has enough
                if freq_map[curr] < active:
                    return False

                # update curr num after moving it to group
                added = freq_map[curr] - active

                # the rest of curr num starts new groups
                active += added
                queue.append(added)
                freq_map[curr] = 0
                
                curr += 1
        
        return True