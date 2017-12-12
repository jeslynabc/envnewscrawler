import requests
from bs4 import BeautifulSoup

def getFreqDict(url):
    wordlist = []
    response = requests.get(url)
    html_code = BeautifulSoup(response.content, "html.parser")
    content = html_code.get_text().lower()

    wordlist = content.split()
    freqdict = wordlisttoFreqDict(wordlist)
    sortdict = sortFreqDict(freqdict)

    with open('scrapper/content.txt', 'w') as file:
        for s in sortdict:
            file.writelines(str(s) + '\n')

def wordlisttoFreqDict(wordlist):
    wordfreq = []
    for w in wordlist:
        wordfreq.append(wordlist.count(w))
    return dict(zip(wordlist, wordfreq))

def sortFreqDict(freqdict):
    aux = []
    for key in freqdict:
        aux.append((freqdict[key], key))
    aux.sort()
    aux.reverse()
    return aux

def removeStopWords():
    #remove common words and symbols
    pass
