import tweepy

access_token = "408180916-lexLejjnitxJ9128aL42twu8pEB1CtSy1dCJtO5V"
access_token_secret = "Ot3laTPsDueEOFnjzj4gEm4wJq0AkQAlQSZMydV9HMgOD"
consumer_key = "9L9LLLYE6fc7jsHo1WjVj8I9f"
consumer_secret = "GDMh9ZxOGbOLOVAqUDLlB3M7R4DWn4QnUFSa8rMmZmc2y3NUfo"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



