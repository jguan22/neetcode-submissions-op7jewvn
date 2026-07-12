class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # greedy: always try to pair a max weight with a min weight using two pointers
        n = len(people)
        people.sort(reverse=True)   # sort the list to use two pointers: O(nlogn)
        
        # loop through the list: O(n)
        l, r = 0, n-1
        count = 0
        while l <= r:
            # either two person if possible
            if people[l] + people[r] <= limit:
                l += 1
                r -= 1
            else:   # or one person with max weight
                l += 1
            
            count += 1
        
        return count