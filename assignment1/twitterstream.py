'''
UW - Data Manipulation at Scale: Systems and Algorithms

Assignment 1: Twitter Sentiment Analysis

Problem 1: Get Twitter Data

Grab tweets data and store it in file

Example:
$ python twitterstream.py > output.txt

'''

import oauth2 as oauth
import urllib2 as urllib

# See assignment1.html instructions or README for how to get these credentials

api_key = "BT3enQIAFJh3OCHwm9S7SqwEv"
api_secret = "s799rnJ3LqwXYIUCMznGIJLVpZZxZIRbWmRcc498gwAbNia70N"
access_token_key = "218951411-36p5ZRl8JgEW6HPxK64NDWyr4Ul7zuK9saJinPvV"
access_token_secret = "J0J1225whaZSLPO9H7c6S05LUm7kKYweRvk73eyi74M55"

_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=api_key, secret=api_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitterreq(url, method, parameters):
  req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url, 
                                             parameters=parameters)

  req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

  headers = req.to_header()

  if http_method == "POST":
    encoded_post_data = req.to_postdata()
  else:
    encoded_post_data = None
    url = req.to_url()

  opener = urllib.OpenerDirector()
  opener.add_handler(http_handler)
  opener.add_handler(https_handler)

  response = opener.open(url, encoded_post_data)

  return response

def fetchsamples():
  url = "https://stream.twitter.com/1.1/statuses/sample.json"
  parameters = []
  response = twitterreq(url, "GET", parameters)
  for line in response:
    print line.strip()

if __name__ == '__main__':
  fetchsamples()
