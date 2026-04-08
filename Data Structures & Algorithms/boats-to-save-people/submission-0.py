class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # each boat can fit two people at top
        # idea is to fit high first, add low if possible
        people.sort()
        n = len(people)
        count = 0
        l, r = 0, n-1
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1

            r -= 1
            count += 1
    
        return count