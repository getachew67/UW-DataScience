'''
UW - Data Manipulation at Scale: Systems and Algorithms

Assignment 1: Twitter Sentiment Analysis

Problem 3: Derive the sentiment of new terms

Computes the sentiment for the terms that do not appear in the file AFINN-111.txt.

Example:
$ python term_sentiment.py AFINN-111.txt output.txt
or
$ python term_sentiment.py

foo 103.256
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


def find_new_terms(lst_of_words_lst, old_terms):
	new_terms = list()
	for words_lst in lst_of_words_lst:
		words = list(set(words_lst))
		new_terms += [t for t in words
						if t not in old_terms]

	return list(set(new_terms))


def new_term_scores(new_terms, t_scores, scores):
	for t in new_terms:
		sum_score = 0
		count = 0
		for entry in t_scores:
			if t not in entry[0]: continue
			sum_score += entry[1]
			count += entry[0].count(t)
		
		if count == 0: print t, 0.0
		else: print t, 1.0*sum_score/count


def main():
	try: sent_file = open(sys.argv[1])
	except: sent_file = open('AFINN-111.txt')
	try: tweet_file = open(sys.argv[2])
	except: tweet_file = open('three_minutes_tweets.json')

	# Generate term scores dictionary

	scores = term_scores(sent_file)


	# Derive the sentiment of each tweet

	t_scores = tweet_scores(tweet_file, scores)

	
	# Find new terms in tweets
	lst_of_words_lst = [entry[0] for entry in t_scores]
	old_terms = [t.decode('utf-8') for t in scores.keys()]
	new_terms = find_new_terms(lst_of_words_lst, old_terms)
	print 'Number of new terms:', len(new_terms)


	# Derive the sentiment of new terms
	new_term_scores(new_terms, t_scores, scores)



if __name__ == '__main__':
    main()
