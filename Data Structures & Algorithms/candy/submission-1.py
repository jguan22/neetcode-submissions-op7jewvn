class Solution:
    def candy(self, ratings: List[int]) -> int:
        # sort the ratings and give 1 candy to local lowest
        # plus 1 for its neighbours
        new_list = [(rating, i+1) for i, rating in enumerate(ratings)]
        new_list.sort(key=lambda x:x[0])

        ratings = [0] + ratings + [0]
        n = len(ratings)
        memo = [0] * n

        for rating, i in new_list:
            # ensure it has more candy if it has higher rating
            if rating > ratings[i-1]:
                memo[i] = max(memo[i], memo[i-1] + 1)
            if rating > ratings[i+1]:
                memo[i] = max(memo[i], memo[i+1] + 1)
            
            # local min
            if memo[i] == 0:
                memo[i] = 1
        
        return sum(memo)