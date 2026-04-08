class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def computeTime(capacity):
            time = 1
            curr_w = 0
            for w in weights:
                if curr_w + w > capacity:
                    curr_w = 0
                    time += 1
                
                curr_w += w
            return time
                    

        l, r = max(weights), sum(weights)
        while l < r:
            mid = (l+r) // 2
            t = computeTime(mid)
            if t > days:
                l = mid + 1
            else:
                r = mid
        
        return l