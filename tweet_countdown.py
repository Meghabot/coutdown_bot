import os
import tweepy
import datetime
import time

# Step 1: Authenticate to Twitter
api_key = os.getenv("API_KEY")
api_secret_key = os.getenv("API_SECRET_KEY")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

# Setting up the authentication
auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Step 2: Calculate the countdown
def days_until_release():
    release_date = datetime.datetime(2024, 12, 6)
    today = datetime.datetime.now()
    countdown_days = (release_date - today).days
    return countdown_days

# Step 3: Compose and post the tweet
def post_tweet():
    countdown_days = days_until_release()
    tweet_content = f"{countdown_days} days until #Pushpa2TheRule hits the screens! 🎬"
    try:
        api.update_status(tweet_content)
    except tweepy.errors.TweepyException as e:
        print(f"Error during authentication or posting: {e}")

# Step 4: Schedule the tweet to post every day at 12:00 AM
while True:
    now = datetime.datetime.now()
    if now.hour == 0 and now.minute == 0:
        post_tweet()
        # Sleep for 24 hours after tweeting
        time.sleep(86400)
    else:
        # Sleep for 1 minute before checking the time again
        time.sleep(60)
