'''
UW - Data Manipulation at Scale: Systems and Algorithms

Assignment 1: Twitter Sentiment Analysis

Problem 2: Derive the sentiment of each tweet

Compute the sentiment of each tweet based on the sentiment scores of the terms in the
tweet. Each word or phrase found in a tweet, but not in AFINN-111.txt should be given
a sentiment score of 0.

Example:
$ python tweet_sentiment.py AFINN-111.txt output.txt
or
$ python tweet_sentiment.py

0.0
1.0
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


def tweet_scores(tweet_file, scores):
	t_scores = list()
	for line in tweet_file:
		if line.startswith('{"delete":'): continue
		tweet_text = json.loads(line)['text']
		words = tweet_cleaning(tweet_text)

		score = words_score(words, scores)
		t_scores.append([words, score])

	return t_scores



def main():
	try: sent_file = open(sys.argv[1])
	except: sent_file = open('AFINN-111.txt')
	try: tweet_file = open(sys.argv[2])
	except: tweet_file = open('three_minutes_tweets.json')

	# Generate term scores dictionary

	scores = term_scores(sent_file)


	# Derive the sentiment of each tweet

	t_scores = tweet_scores(tweet_file, scores)


	# stdout scores in file
	t_scores_file = open('sentiment_scores.txt','w')

	for entry in t_scores:
		t_scores_file.write(str(entry[1]))
		t_scores_file.write('\n')
	t_scores_file.close()


if __name__ == '__main__':
    main()
