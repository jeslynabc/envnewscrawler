# envnewscrawler

A crawler to crawl news sites and generate a sentiment score for environmental news using Python.

Input: URL of news sites' main pages (with all the article titles)  
Output: Sentiment score for each article

## Overview
1. Build the lexicon we will use to identify environment-related news (keyword matching)
- Identify keywords related to the environment. Possible sources:
  - Online
  - Thesaurus
  - Scrapping from environmental related websites
2. Find news sites to crawl from 
- SG e.g. ST, CNA
- Worldwide e.g. BBC, Guardian
3. Compute sentiment score
- Using NLTK (nltk.vader)

## Implementation 

### Part 1

Once we have found words related to environmental issues, we can save our lexicon into a .csv file.

### Part 2
Input: URL
Output: Articles related to the environment

1. Fetch the raw html code from the given URL using requests.get()
2. Identify patterns in code to sieve out what we are interested in (article links and article titles)
3. Check whether each word in the title can be found in the lexicon. Filter out those that are below the threshold number of words in the title.
4. Visit the links of the remaining article to retrieve the article's text.

### Part 3
Input: Articles
Output: Sentiment score

1. Perform sentiment analysis using nltk.vader in NLTK


## Possible extensions
0. Apply this to CNA, ST, and any other SG news sites to get an aggregate score.
1. Develop a better lexicon