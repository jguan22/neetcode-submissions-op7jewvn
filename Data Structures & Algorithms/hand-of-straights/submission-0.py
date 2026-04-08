class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False
            
        card_map = defaultdict(int)
        for card in hand:
            card_map[card] += 1
        
        min_heap = list(card_map.keys())
        heapq.heapify(min_heap)

        # starting from the lowest card
        while min_heap:
            card = min_heap[0]
            num = card_map[card]

            if num == 0:
                heapq.heappop(min_heap)
                continue

            for i in range(groupSize):
                card_map[card+i] -= num
                if card_map[card+i] < 0:
                    return False

        return True   