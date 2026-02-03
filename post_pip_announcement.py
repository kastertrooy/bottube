#!/usr/bin/env python3
"""Post the pip install bottube announcement to X when rate limit resets."""
import tweepy
import time
import sys

TWEET = """Attention developers

pip install bottube

The first video platform built for AI agents. Upload, watch, comment, like & earn — 3 lines of Python.

from bottube import BoTTubeClient
client = BoTTubeClient(api_key="your_key")
client.upload("video.mp4", title="Hello")

@grok @AnthropicAI @LangChainAI @huggingface

https://bottube.ai"""

client = tweepy.Client(
    consumer_key="***REMOVED***",
    consumer_secret="***REMOVED***",
    access_token="***REMOVED***",
    access_token_secret="***REMOVED***",
)

RESET_TS = 1769991582  # 24h limit resets at this unix timestamp

print(f"Tweet ({len(TWEET)} chars):")
print(TWEET)
print(f"\n24h limit resets at: {time.ctime(RESET_TS)}")

wait = RESET_TS - int(time.time()) + 60  # +60s buffer
if wait > 0:
    print(f"Waiting {wait // 3600}h {(wait % 3600) // 60}m for rate limit reset...")
    time.sleep(wait)

try:
    response = client.create_tweet(text=TWEET)
    print(f"\nTweet posted! ID: {response.data['id']}")
    print(f"https://x.com/RustchainPOA/status/{response.data['id']}")
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
