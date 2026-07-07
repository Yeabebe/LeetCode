from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)      # user -> [(time, tweetId)]
        self.following = defaultdict(set)    # user -> followees

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []

        users = self.following[userId] | {userId}

        for user in users:
            if self.tweets[user]:
                idx = len(self.tweets[user]) - 1
                time, tweet = self.tweets[user][idx]
                heapq.heappush(heap, (-time, tweet, user, idx))

        feed = []

        while heap and len(feed) < 10:
            neg_time, tweet, user, idx = heapq.heappop(heap)
            feed.append(tweet)

            if idx > 0:
                idx -= 1
                time, tweet = self.tweets[user][idx]
                heapq.heappush(heap, (-time, tweet, user, idx))

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)


