'''
UW - Data Manipulation at Scale: Systems and Algorithms

Assignment 1: Twitter Sentiment Analysis

Problem 6: Top ten hash tags

Computes the ten most frequently occurring hash tags from a tweet file.

Example:
$ python top_ten.py output.txt
or
$ python top_ten.py

bar 30
...

'''

import sys
import json

def hashtag_freq(tweet_file):
	hashtags = dict()
	for line in tweet_file:
		if line.startswith('{"delete":'): continue
		tweet_tags = json.loads(line)['entities']['hashtags']
		if len(tweet_tags) == 0: continue
		for t in tweet_tags:
			hashtags[t['text']] = hashtags.get(t['text'],0)+1

	return hashtags


def main():
	try: tweet_file = open(sys.argv[1])
	except: tweet_file = open('three_minutes_tweets.json')

	# Get the dictionary of hashtags and the frequency
	hashtags = hashtag_freq(tweet_file)

	# Sort and print the top ten hashtags
	hashtags = sorted(hashtags.items(), key=lambda h:h[1], reverse=True)
	for i in range(10):
		print hashtags[i][0], hashtags[i][1]


if __name__ == '__main__':
    main()
