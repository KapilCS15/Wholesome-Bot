import praw
import random
import time

reddit = praw.Reddit(
    client_id="POks8SG_SAKjttePjc5M7w",
    client_secret="xgtGdnuEV0120xNILAdXkXB6m3oA-A",
    user_agent="<console:WHOLESOME:2.0>",
    username="Wholesome-Bot2",
    password="Ironpatriot@5"
)
subreddit = reddit.subreddit("television")
wholesome_quotes=["The past is gone, the future is not here, now I am free of both. Right now, I choose joy. -Deepak Chopra",
"Although the world is full of suffering, it is also full of the overcoming of it. -Helen Keller",
"Pain is temporary. It may last a minute, or an hour, or a day, or a year, but eventually it will subside and something else will take its place. -Lance Armstrong",
"Yesterday is not ours to recover, but tomorrow is ours to win or lose. -Lyndon B. Johnson",
"The way I see it, if you want the rainbow, you gotta put up with the rain! -Dolly Parton",
"If somebody hurts you, it’s okay to cry a river: Just remember to build a bridge and get over it. -Taylor Swift"]

for submission in subreddit.hot(limit=10):
    print("*****")
    print(submission.title)

    for comment in submission.comments:
        if hasattr(comment,"body"):
            comment_lower=comment.body.lower()
            if" sad " in comment_lower:
                print("------")
                print(comment.body)
                random_index=random.randint(0,len(wholesome_quotes)-1)
                comment.reply(wholesome_quotes[random_index])
                time.sleep(660)