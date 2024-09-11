import os
import tweepy
import datetime

# Authenticate to Twitter
api_key = os.getenv("API_KEY")
api_secret_key = os.getenv("API_SECRET_KEY")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def days_until_release():
    release_date = datetime.datetime(2024, 12, 6)
    today = datetime.datetime.now()
    countdown_days = (release_date - today).days
    return countdown_days

def post_tweet():
    countdown_days = days_until_release()
    tweet_content = f"{countdown_days} days until #Pushpa2TheRule hits the screens! 🎬"
    print(f"Tweet content: {tweet_content}")  # Debug print
    try:
        api.update_status(tweet_content)
        print("Tweet posted successfully.")
    except tweepy.TweepyException as e:
        print(f"Error during posting: {e}")

now = datetime.datetime.now()
if now.hour == 0 and now.minute == 0:
    post_tweet()
else:
    print("Not the scheduled time. Skipping tweet.")
