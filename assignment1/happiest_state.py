'''
UW - Data Manipulation at Scale: Systems and Algorithms

Assignment 1: Twitter Sentiment Analysis

Problem 5: Which State is happiest?

Returns the code of the happiest state as a string.

Example:
$ python happiest_state.py AFINN-111.txt output.txt
or
$ python happiest_state.py

bar 30
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


def term_scores(sent_file):
	scores = dict()
	for line in sent_file:
		term, score  = line.split("\t")
		scores[term] = int(score)
	return scores


def words_score(words_lst, scores):
	return sum(scores.get(w, 0) for w in words_lst)


def geo_info(tweet):
	try:
		country = tweet['place']['country_code']
		state = tweet['place']['full_name'].split(', ')[-1]
		return country, state
	except:
		return None, None


def state_happiness(tweet_file, scores):
	state_count = dict()
	state_score = dict()

	for line in tweet_file:
		if line.startswith('{"delete":'): continue
		tweet = json.loads(line)
		if line.startswith('{"delete":'): continue

		country, state = geo_info(tweet)
		if country != 'US' or len(state) != 2: continue


		score = words_score(tweet_cleaning(tweet['text']), scores)
		state_count[state] = state_count.get(state, 0)+1
		state_score[state] = state_score.get(state, 0)+score

	return {state: state_score[state]/state_count[state]
						for state in state_count.keys()}


def main():
	try: sent_file = open(sys.argv[1])
	except: sent_file = open('AFINN-111.txt')
	try: tweet_file = open(sys.argv[2])
	except: tweet_file = open('three_minutes_tweets.json')

	# Generate term scores dictionary

	scores = term_scores(sent_file)


	# Derive the sentiment of each tweet
	tweet_file = open(sys.argv[2])

	# Find the happiness scores for each state
	happiness = state_happiness(tweet_file, scores)

	happiest_state = max(happiness, key=happiness.get)
	print happiest_state, happiness[happiest_state]


if __name__ == '__main__':
    main()
