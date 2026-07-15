class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search the answer, ans is bounded by the largest pile
        lo, hi = 1, max(piles)

        def eat(n):
            t = 0
            for pile in piles:
                t += math.ceil(pile / n)
            return t

        while lo < hi:
            mid = (lo + hi) // 2
            if eat(mid) > h:
                lo = mid + 1
            else:
                hi = mid
        
        return lo