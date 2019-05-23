import twitter
import twitter_credentials

api = twitter.Api(consumer_key=twitter_credentials.CONSUMER_KEY,
                  consumer_secret=twitter_credentials.CONSUMER_SECRET,
                  access_token_key=twitter_credentials.ACCESS_TOKEN,
                  access_token_secret=twitter_credentials.ACCESS_TOKEN_SECRET)


print(api.VerifyCredentials())
output_list = api.GetSearch(geocode="37.781157,-122.398720,1mi")
print(output_list)
