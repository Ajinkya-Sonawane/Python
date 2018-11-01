import pandas as pd
from sklearn.model_selection import train_test_split

import nltk
from nltk.corpus import stopwords


POSITIVE = 4
NEGATIVE = 0
NEUTRAL = 2

#Read the data
data = pd.read_csv('twitter1.csv')

#Split into train and test
train,test = train_test_split(data,test_size = 0.2)

#Remove neutral tweets
train = train[train.target != NEUTRAL]
test_pos = test[test['target'] == POSITIVE]['text']
test_neg = test[test['target'] == NEGATIVE]['text']

tweets = []

#Create set of stopwords using nltk
stopwords = set(stopwords.words("english"))

#Filter the tweets
for index,row in train.iterrows():
    words_filtered = []
    for word in row.text.split():
        if not((len(word)<3)or
               (word.startswith('@'))or
               (word.startswith('#'))or
               (word in stopwords)or
               ('http' in word)):
               words_filtered.append(word)

    tweets.append((words_filtered,row.target))

#Function to extract words from tweets   
def get_words_in_tweets(tweets):
    wordList = []
    for (words,sentiment) in tweets:
        wordList.extend(words)
    return wordList

#Function to extract words based on their frequency
def get_word_features(wordList):
    wordList = nltk.FreqDist(wordList)
    features = wordList.keys()
    return features

#Function to extract words based on document features
def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features


wordList = get_words_in_tweets(tweets)
word_features = get_word_features(wordList)

training_set = nltk.classify.apply_features(extract_features,tweets,labeled=True)
classifier = nltk.NaiveBayesClassifier.train(training_set)

tp,tn,fp,fn = 0,0,0,0

for tweet in test_neg:
    res = classifier.classify(extract_features(tweet.split()))
    if res == NEGATIVE:
        tn +=1
    else:
        fp += 1

for tweet in test_pos:
    res = classifier.classify(extract_features(tweet.split()))
    if res == POSITIVE:
        tp +=1
    else:
        fn += 1
acc = (tp+tn)/(tp+tn+fp+fn)
print('Accuracy : ',acc*100)
