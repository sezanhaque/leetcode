import itertools, collections, heapq


class Twitter:
    def __init__(self):
        self.post = 0
        self.tweets = collections.defaultdict(collections.deque)
        self.followees = collections.defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].appendleft((self.post, tweetId))
        self.post -= 1

    def getNewsFeed(self, userId: int) -> list[int]:
        tweets = heapq.merge(
            *(self.tweets[user] for user in self.followees[userId] | {userId})
        )
        return (tweet for _, tweet in itertools.islice(tweets, 10))
        # return (tweet for _, tweet in heapq.nsmallest(10, tweets))

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
obj = Twitter()
obj.postTweet(1, 5)
obj.getNewsFeed(1)
obj.follow(1, 2)
obj.postTweet(2, 6)
obj.getNewsFeed(1)
obj.unfollow(1, 2)
obj.getNewsFeed(1)
