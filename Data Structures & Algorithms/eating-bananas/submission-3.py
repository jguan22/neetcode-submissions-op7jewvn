class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def computeTime(num):
            time = 0
            for pile in piles:
                # time += math.ceil(pile / num) or use integer division trick
                time += (pile + num - 1) // num
            return time
        
        l, r = 1, max(piles)
        while l < r:
            mid = (l+r) // 2
            t = computeTime(mid)
            if t > h:
                l = mid + 1
            else:
                r = mid
        
        return l