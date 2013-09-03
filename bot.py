import time
import praw
r = prawa.Reddit('PRAW related-question monitor by u/_Daimon_ v 1.0. '
...                 'Url: https://praw.readthedocs.org/en/latest/'
...                 'pages/writing_a_bot.html')
r.login()
already_done = []

while True:
	subreddit = r.get_subreddit('learnpython')
	for submission in subreddit.get_hot(limit=10):
		
