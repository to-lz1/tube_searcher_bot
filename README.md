# tube_searcher_bot

Crawl YouTube, and tweet video URL using Twitter API.

### usage

#### make config.py like below.

```.py

CONSUMER_KEY        = "CONSUMER_KEY of Your Twitter App"
CONSUMER_SECRET     = "CONSUMER_SECRET of Your Twitter App"
ACCESS_TOKEN        = "ACCESS_TOKEN of Your Twitter App"
ACCESS_TOKEN_SECRET = "ACCESS_TOKEN_SECRET of Your Twitter App"

REPLY_TO = [
    "Twitter_Account_Name(optional. without '@')"
]

KEYWORDS = [
    "key word as you like",
    "another key word"
]
CHANNELS = [
    "id_of_favorite_list",
    "another_one",
    ...
]

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

command below makes .zip file that is executable as AWS Lambda handler.

```
$ ./package_lambda.sh
```

because handler is within `tube_searcher_bot` package, handler function name will be `tube_searcher_bot.process.lambda_handler`.