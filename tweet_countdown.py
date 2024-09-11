import os
import tweepy
from datetime import datetime

# Fetching Twitter API credentials from environment variables
api_key = os.getenv('API_KEY')
api_secret_key = os.getenv('API_SECRET_KEY')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

# Authenticate with the Twitter API
auth = tweepy.OAuth1UserHandler(api_key, api_secret_key, access_token, access_token_secret)
api = tweepy.API(auth)

# Check if authentication was successful
try:
    api.verify_credentials()
    print("Authentication successful")
except:
    print("Error during authentication")

# Calculate countdown days
release_date = datetime(2024, 12, 6)  # Release date of Pushpa 2: The Rule
today = datetime.now()
days_left = (release_date - today).days

# Prepare the tweet content
tweet_content = f"{days_left} days left until Pushpa 2: The Rule! #Pushpa2TheRule"

# Post the tweet
try:
    api.update_status(tweet_content)
    print(f"Tweeted: {tweet_content}")
except tweepy.TweepError as e:
    print(f"Error posting tweet: {e}")
