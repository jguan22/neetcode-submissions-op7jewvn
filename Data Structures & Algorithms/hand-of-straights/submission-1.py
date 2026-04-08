class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # sanity check
        if len(hand) % groupSize != 0:
            return False

        countMap = Counter(hand)
        order = list(countMap.keys())
        order.sort()

        # check the cards in order from smallest
        for card in order:
            if countMap[card] == 0:
                continue

            curr_count = countMap[card]
            for i in range(groupSize):
                if countMap[card+i] < curr_count:
                    return False
                countMap[card+i] -= curr_count

        return True