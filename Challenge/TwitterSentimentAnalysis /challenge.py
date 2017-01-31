import tweepy
from textblob import TextBlob
#from textblob_fr import PatternTagger, PatternAnalyzer
import csv


#Step 2b - Function of labelisation of analysis
def get_label(analysis, threshold = 0):
	if analysis.sentiment[0]>threshold:
		return 'Positive'
	else:
		return 'Negative'


consumer_key = "[COSUMER_KEY]"
consumer_secret = "[consumer_secret]"
access_token = "[access_token]"
access_token_secret = "[access_token_secret]"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
this_candidate_polarities = []
public_tweets = api.search('Trump', count=100)
with open('thefile.csv', 'w') as this_candidate_file:
    this_candidate_file.write('tweet,sentiment_label\n')
    for tweet in public_tweets:
        analysis = TextBlob(tweet.text)
        print(analysis)
        print(analysis.sentiment[0])
        this_candidate_polarities.append(analysis.sentiment[0])
        this_candidate_file.write('%s,%s\n' % (tweet.text.encode('utf8'), get_label(analysis)))


