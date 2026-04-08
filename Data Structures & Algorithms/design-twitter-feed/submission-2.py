class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((-self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # use max_heap to feed most recent news
        max_heap = self.tweetMap[userId][-10:]
        
        for followeeId in self.followMap[userId]:
            max_heap.extend(self.tweetMap[followeeId][-10:])
        
        heapq.heapify(max_heap)
        res = []
        k = 10
        while max_heap and k > 0:
            res.append(heapq.heappop(max_heap)[1])
            k -= 1
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        # cant follow theirselves
        if followerId == followeeId:
            return 
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
