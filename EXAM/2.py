import os
import re

def maketext(filename):
    with open(filename, encoding = 'utf-8') as f:
        text = f.read()
    return text

def findnames():
    freq = {}
    pages = os.listdir('.')
    for page in pages:
        text = maketext(page)
        names = re.findall('lex="([А-Я][а-я]+?)"', text)
        for name in names:
            if name in freq:
                freq[name] += 1
            else:
                freq[name] = 1
    return freq

def makecsv():
    freq = findnames()
    with open('two.csv', "w", encoding = 'cp1251') as f:
        for k in freq.keys():
            f.write(k + '\t' + str(freq[k]) + '\n')
    return

makecsv()
