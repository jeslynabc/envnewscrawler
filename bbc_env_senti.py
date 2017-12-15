from urllib.parse import urlparse, urljoin
import requests
from bs4 import BeautifulSoup

import csv

import string
from newspaper import Article

import nltk
# nltk.download('vader_lexicon') # corpus that the sentiment analyzer uses
from nltk.sentiment.vader import SentimentIntensityAnalyzer

### Functions used ###

def lexicon_check(news_title):
    number_of_matches = 0
    news_title_list = news_title.lower().split(' ')
    for word in news_title_list:
        if (word in lexicon):
            number_of_matches += 1

    return number_of_matches

def strip_punctuation(s):
    return ''.join(c for c in s if c not in string.punctuation)

def calculate_sentiment(list_of_sentences):
    sid = SentimentIntensityAnalyzer() # does the SA 

    sentiment_sum = 0 

    compound_scores = []

    for sentence in list_of_sentences:
        print(sentence)
        ss = sid.polarity_scores(sentence)
        for k in ss:
            print("{0}: {1}, ".format(k, ss[k]), end='')
            if (k == "compound"):
                compound_scores.append(ss[k])
                # print(ss[k])
                sentiment_sum += ss[k]
        print()
    print("Data length = " + str(len(list_of_sentences)))
    print("Average sentiment score: " + str(sentiment_sum/len(list_of_sentences)))

    return(sentiment_sum)


### Main code ###

# Read in lexicon from .csv file 
lexicon = []
with open('lexicon.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        lexicon.append(row[0].strip()) # our lexicon is in 1 column

# Set URL to scrape articles from
givenurl = "http://www.bbc.com/news/science_and_environment" # input("Enter URL: ")
html_code = requests.get(givenurl)
clean_html = BeautifulSoup(html_code.content,"html.parser")

# Find articles by looking at <a> tags and checking if 'news' is in the URL
news_links = []
for link in clean_html.find_all("a", {'class':'faux-block-link__overlay-link'}):
    parsed_link = urlparse(link.get('href'))
    if 'news' not in parsed_link.path:
        continue 
    else: 
        news_links.append(link)

# Find the environment-related articles by matching title with lexicon
env_related_news = []
for news in news_links:    
    title = strip_punctuation(news.string[13:])
    lexicon_score = lexicon_check(title.lstrip()) # remove whitespace in front of title 

    # if lexicon_score > threshold, we keep it
    if (lexicon_score > 1):
        env_related_news.append(news)

# Perform sentiment analysis on the selected articles
for envnews in env_related_news:
    parsed_link = urlparse(envnews.get('href'))
    article_link = urljoin(givenurl, parsed_link.path)
    article = Article(article_link)
    article.download()
    article.parse()
    article_lines = article.text.splitlines()

    score = calculate_sentiment(article_lines)
    print(score)