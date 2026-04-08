class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search the answer
        lo, hi = 1, max(piles)

        def needTime(n):
            count = 0
            for pile in piles:
                count += math.ceil(pile / n)
            return count

        while lo < hi:
            mid = (lo + hi) // 2
            if needTime(mid) > h:
                lo = mid + 1
            else:
                hi = mid
        
        return lo