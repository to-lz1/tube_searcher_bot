# tube_searcher_bot

Crawl YouTube, and tweet video URL using Twitter API.

### usage

#### make config.py like below.

```.py

CONSUMER_KEY        = "CONSUMER_KEY of Your Twitter App"
CONSUMER_SECRET     = "CONSUMER_SECRET of Your Twitter App"
ACCESS_TOKEN        = "ACCESS_TOKEN of Your Twitter App"
ACCESS_TOKEN_SECRET = "ACCESS_TOKEN_SECRET of Your Twitter App"

REPLY_TO = "Twitter_Account_Name(optional. without '@')"

KEYWORD_1 = "key word as you like"
KEYWORD_2 = "key word as you like, again"
CHANNEL = "id of a channel you love"

```

#### environment

run below:
```
pipenv install
pipenv shell
```

for testing:
```
python -m unittest discover
```

run main.py in local by:
```
python main.py
```

#### package as a AWS Lambda function.

command below makes .zip file that is executable as AWS Lambda handler.(WIP)

```
$ ./package_lambda.sh
```
