# tube_searcher_bot

Crawl YouTube, and tweet video URL using Twitter API.

### usage

#### make config.py

```config.py

CONSUMER_KEY        = "CONSUMER_KEY of Your Twitter App"
CONSUMER_SECRET     = "CONSUMER_SECRET of Your Twitter App"
ACCESS_TOKEN        = "ACCESS_TOKEN of Your Twitter App"
ACCESS_TOKEN_SECRET = "ACCESS_TOKEN_SECRET of Your Twitter App"

REPLY_TO = "Your Twitter Account(optional)"

```

#### package as a AWS Lambda function.

command below makes .zip file that is executable as AWS Lambda handler.

```
$ ./package_lambda.sh
```

#### You can edit main.py as you like.

```main.py
t = TubeCrawler()

movies = t.movies_from_query("key word as you like")
movies += t.movies_from_channel("id of a channel you love")
movies += t.movies_from_list("id of your favorite list")

tw = Tweeter()
chosen = t.choose(movies)
tw.reply(config.REPLY_TO, chosen)
return chosen
```
