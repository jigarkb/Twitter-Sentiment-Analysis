from collections import defaultdict
import simplejson
import sys

##afinnfile = open(sys.argv[1])
##tweet_file = open(sys.argv[2])
afinnfile = open("AFINN-111.txt")
tweet_file = open("twitterstream.txt")
scores = {} 
for line in afinnfile:
    term, score  = line.split("\t")  # The file is tab-delimited. 
    scores[term] = int(score)  # Convert the score to an integer.


tweet = []
text = []
tweets_location = []
tweet_words = []
tweet_item = []
tweet_score=0
tweet_dict={}
j=0
for line in tweet_file:
    data=simplejson.loads(line)
    if not data.has_key('text'): 
        continue
    text.append(data['text'].lower())
    tweet.append(text[j])
    tweets_location.append(data['user']['location'].lower())
    j+=1
    
for item in tweet:
    tweet_words.append(item.split()) #Append list of words for each tweet to corrosponding tweet_words
    
for item in tweet_words: #Count and add score of each word of a tweet
    tweet_score=0
    for w in item:
        if w in scores:
            tweet_score+=scores[w]
        else:
            tweet_score+=0
    tweet_item.append(tweet_score)
	
for i in range(len(tweet_item)):
    tweet_dict[tweet[i]]=[tweet_item[i],tweets_location[i]]
    
with open('tweets_sentiment.txt', 'w') as outfile: #Store Dictionary as {Tweet_Text:[Score,Location]}
  simplejson.dump(tweet_dict, outfile)                

                
D=defaultdict(list)
L={}
for i,item in enumerate(tweets_location):
    D[item].append(i)
for key in D:
    sum1=0
    for item in D[key]:
        sum1+=tweet_item[item]
    L[key]=sum1
with open('location_sentiment.txt', 'w') as outfile: #Store Dictionary as {Location:Sum of score for that location}
  simplejson.dump(L, outfile) 
