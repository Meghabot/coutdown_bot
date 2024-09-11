import os
import tweepy
from datetime import datetime

# Fetching Twitter API credentials from environment variables
api_key = os.getenv('API_KEY')
api_secret_key = os.getenv('API_SECRET_KEY')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

# Authenticate with the Twitter API
auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Calculate countdown days
release_date = datetime(2024, 12, 6)
today = datetime.now()
days_left = (release_date - today).days

# Prepare the tweet content
tweet_content = f"{days_left} days left until Pushpa 2: The Rule! #Pushpa2TheRule"

# Post the tweet
api.update_status(tweet_content)
print(f"Tweeted: {tweet_content}")
