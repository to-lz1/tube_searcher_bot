from tube_searcher_bot import api_auth

class Tweeter:
    def tweet(self, text):
        twAuth = api_auth.getOAuth()
        apiURL = "https://api.twitter.com/1.1/statuses/update.json"
        params = { "status": text }
        twAuth.post(apiURL, params = params)

    def reply(self, to, text):
        self.tweet("@" + to + " " + text)
