import heapq
class Twitter:
    def __init__(self):
        self.follows = {}
        self.posts = {}
        self.tweets_count = 0
        self.followers = {}
    def postTweet(self, userId, tweetId):
        current_count = self.tweets_count
        self.tweets_count -= 1
        if userId in self.posts:
            self.posts[userId].add((current_count, tweetId))
        else:
            self.posts[userId] = {(current_count, tweetId)}
    def getNewsFeed(self, userId):
        news_feed = []
        if userId in self.follows:
            for followeeId in self.follows[userId]:
                if followeeId in self.posts:
                    for tweet in self.posts[followeeId]:
                        heapq.heappush(news_feed, tweet)
        if userId in self.posts:
            for tweet in self.posts[userId]:
                heapq.heappush(news_feed, tweet)
        posts_to_display = []
        for _ in range(10):
            if len(news_feed) == 0:
                break
            _, tweetId = heapq.heappop(news_feed)
            posts_to_display.append(tweetId)
        return posts_to_display
    def follow(self, followerId, followeeId):
        if followerId in self.follows:
            self.follows[followerId].add(followeeId)
        else:
            self.follows[followerId] = {followeeId}
        if followeeId in self.followers:
            self.followers[followeeId].add(followerId)
        else:
            self.followers[followeeId] = {followerId}
    def unfollow(self, followerId, followeeId):
        if followerId in self.follows:
            self.follows[followerId].remove(followeeId)
        self.followers[followeeId].remove(followerId)
    def suggestUsers(self, userId):
        suggest_users = []
        users_count = 0
        user_follows = set(self.follows[userId])
        users_followers = set(self.followers[userId])
        users_followers_unfollowees = users_followers  - user_follows 
        if len(users_followers_unfollowees) > 20:
            while  len(users_followers_unfollowees) > 20:
                users_followers_unfollowees.pop()
            return users_followers_unfollowees
        else:
            users_count = len(users_followers_unfollowees)
            if users_count == 20:
                return users_followers_unfollowees
        suggest_users = users_followers_unfollowees
        aux_heap = []
        for followee_id in self.follows[userId]:
            if followee_id in self.follows:
                for id in self.follows[followee_id]:
                    if id not in user_follows and id in self.follows:
                        heapq.heappush(aux_heap, abs(set(self.follows[id]) - set(self.follows[userId]), id))                          
        while len(suggest_users) < 20:
            suggest_users.append(heapq.heappop(aux_heap)[1])
        return suggest_users