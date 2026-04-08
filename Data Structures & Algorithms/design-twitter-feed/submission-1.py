class Twitter:

    def __init__(self):
        # need to dict to track following list of each user
        self.follow_list = defaultdict(set)

        # track tweet list
        self.tweet_list = defaultdict(list)
        self.time = 0
        self.feed_number = 10

    def postTweet(self, userId: int, tweetId: int) -> None:
        # use a list with time
        self.tweet_list[userId].append((-self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # use a heap to track tweet time
        max_heap = []
        
        # add user's own tweets
        user_tweets = self.tweet_list[userId][-10:]
        for tweet in user_tweets:
            heapq.heappush(max_heap, tweet)

        # add followee's tweets
        for followee in self.follow_list[userId]:
            tweets = self.tweet_list[followee][-10:]
            for tweet in tweets:
                heapq.heappush(max_heap, tweet)
        
        feed = []
        feed_num = self.feed_number
        while max_heap and feed_num > 0:
            _, tweet = heapq.heappop(max_heap)
            feed.append(tweet)
            feed_num -= 1
        
        return feed


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.follow_list[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follow_list[followerId].discard(followeeId)
