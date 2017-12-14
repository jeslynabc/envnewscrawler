# envnewscrawler

A crawler to crawl news sites and generate sentiment score for environmental news using python.

Input: URL of news sites  
Output: Sentiment score

## Overview
1. Build the lexicon we will use to identify environment-related news (keyword matching)
- Identify keywords related to the environment (lexicon)
  - Online
  - Thesaurus
  - Scrapping from environmental related websites
2. Find news sites to crawl from 
- SG e.g. ST, CNA
- Worldwide e.g. BBC, Guardian
3. Compute sentiment score
- Using NLTK (nltk.vader)

## Getting Started

Input: raw html/htm file

Read all the lines from file -> save it into a list
Create another empty list 

For each line in the list
    check whether 'title-link__title-text' is inside the line
    if inside:
        store into the new list
    else: (if not inside)
        continue 

end goal: find lines that contain 'title-link__title-text'