class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n  # Everyone gets at least 1
        
        # Left to Right: Check left neighbor
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        
        # Right to Left: Check right neighbor
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i+1]:
                # Must be higher than right neighbor AND keep its L-to-R value
                candies[i] = max(candies[i], candies[i+1] + 1)
        
        return sum(candies)