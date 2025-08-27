# X (Twitter) Design  

The passion for developing this project came after solving **[LeetCode 355. Design Twitter](https://leetcode.com/problems/design-twitter/)**, which was one of the problems I enjoyed the most solving.”

The original problem was about implementing a few core features of a social media platform like X (formerly Twitter):   `postTweet`, `getNewsFeed`, `follow`, `unfollow`  

After finishing those, I still felt motivated to expand it 😀. So I thought about adding more features such as: `suggestUsers`, `likeHandler`, `commentHandler`, `editPost`, `deletePost`, `message` ...

I am not building a production-ready app, linking a NoSQL backend, or exposing a REST API. Instead, this project focuses purely on the logic behind these features, implemented through a `Twitter` class and its methods.  

---

## Features implemented so far

### `postTweet`
Checks if the current user has posted before. If yes, it adds the `(timestamp, tweetId)` to the user’s posts. Otherwise, it creates a new post set for that user.  

### `getNewsFeed`  
Retrieves the 10 most recent tweets in a user’s news feed. The feed includes tweets from users the person follows as well as their own tweets, ordered from most recent to least recent.  

### `follow`  
Makes a user (`followerId`) follow another user (`followeeId`). Updates both the `follows` and `followers` mappings.  

### `unfollow`  
Makes a user (`followerId`) unfollow another user (`followeeId`). Removes the relationship from both `follows` and `followers`.  

### `suggestUsers`  
Suggests up to 20 new users that the current user might want to follow.  
- First, it recommends users who follow the current user but whom the user hasn’t followed back.  
- If that’s not enough, it also looks at the people followed by the current user’s followees (friends of friends) and ranks them by popularity (how many mutual connections they share).

---

## Usage  

```python
# Example usage
obj = Twitter()
obj.postTweet(userId=1, tweetId=101)
feed = obj.getNewsFeed(userId=1)
obj.follow(followerId=1, followeeId=2)
obj.unfollow(followerId=1, followeeId=2)
suggestions = obj.suggestUsers(userId=1)