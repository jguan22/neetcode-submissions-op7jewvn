class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # the min capacity is the max in weights
        # the potential max capacity is total weight
        l, r = max(weights), sum(weights)

        # binary search the capacity
        while l < r:
            mid = l + (r-l) // 2

            # compute cost
            cost = 1
            total = 0
            for weight in weights:
                if total + weight > mid:
                    # overweighted, starting a new day
                    cost += 1
                    total = 0
                total += weight
            
            if cost <= days:
                r = mid
            else:
                l = mid + 1
        
        return l