import time
import praw

user_agent = ("Repostbot /u/darkrai9292 "
               "https://github.com/darkrai9292/Repost-Bot")

r = praw.Reddit(user_agent=user_agent)
r.login()

user_name = "darkrai9292"
user = r.get_redditor(user_name)

limit = 20
gen = user.get_submitted(limit=limit)

karma_by_subreddit = {}
for thing in gen:
	subreddit = thing.subreddit.display_name
	karma_by_subreddit[subreddit] = (karma_by_subreddit.get(subreddit, 0) + thing.score)

print str(karma_by_subreddit)