import praw
import datetime as dt

reddit = praw.Reddit(client_id='####',
                     client_secret='#######',
                     user_agent='my user agent')

#subreddit = reddit.subreddit('reviews')
submission = reddit.submission(id='9w14xq')
#fh=open('reddit.txt','a')
for top_level_comment in submission.comments:
    #print dt.datetime.fromtimestamp(submission.created),submission.title
#for comment in reddit.subreddit('bollywood').stream.comments():
    print dt.datetime.fromtimestamp(submission.created),top_level_comment.body

