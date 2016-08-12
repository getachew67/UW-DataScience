'''
UW - Data Manipulation at Scale: Systems and Algorithms

Assignment 1: Twitter Sentiment Analysis

Problem 4: Compute Term Frequency

Print relative word frequency in a Twitter Stream file.

Example:
$ python frequency.py output.txt
or
$ python frequency.py

bar 0.1245
...

'''

import sys
import json
import re

def tweet_cleaning(ustring):
	ustring = ustring.lower()
	ustring = re.sub(ur'@\S*', ' ', ustring)
	ustring = re.sub(ur'\S*[0-9]+\S*', ' ', ustring)
	ustring = re.sub(ur'http\S*', ' ', ustring)
	ustring = re.sub(ur'\S*.com\S*', ' ', ustring)
	for i in ustring:
		if i != '_' and i !='\'' and not i.encode('utf-8').isalpha():
			ustring = ustring.replace(i, ' ')

	return ustring.split()

def find_words(tweet_file):
	terms = list()
	for line in tweet_file:
		if line.startswith('{"delete":'): continue
		tweet_text = json.loads(line)['text']
		terms += tweet_cleaning(tweet_text)
	return terms


def main():
	try: tweet_file = open(sys.argv[1])
	except: tweet_file = open('three_minutes_tweets.json')

	# Collect the contents of each tweet
	words = find_words(tweet_file)
	countall = len(words)
	print 'Number of words:', len(words)

	# Find unique terms in tweets
	terms = list(set(words))
	print 'Number of terms:', len(terms)
	print ''

	# Derive the freq of terms
	for t in terms:
		count = words.count(t)
		print t, 1.0*count/countall


if __name__ == '__main__':
    main()
