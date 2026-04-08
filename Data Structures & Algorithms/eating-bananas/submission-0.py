class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search the eating speed
        hi = max(piles)
        lo = 1

        # need to find the upper bound of hours
        while lo < hi:
            mid = (hi + lo) // 2

            # compute how many hours koko finishs\
            hours = 0
            for pile in piles:
                # always round up
                hours += math.ceil(pile / mid)
            
            if hours > h:
                # need to eat faster
                lo = mid + 1
            else:
                hi = mid
        
        return lo