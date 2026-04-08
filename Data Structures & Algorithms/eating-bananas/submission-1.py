class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search the eating speed
        n = max(piles)
        l, r = 1, n
        while l < r:
            mid = l + (r-l) // 2
            t = 0
            for pile in piles:
                t += math.ceil(pile / mid)
            
            if t <= h:
                r = mid
            else:
                l = mid + 1
        
        return l