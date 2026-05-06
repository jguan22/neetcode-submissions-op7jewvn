class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        people.sort(reverse=True)
        boat = 0
        l, r = 0, n - 1

        while l <= r:
            if people[l] + people[r] <= limit:
                r -= 1
            l += 1
            boat += 1

        return boat