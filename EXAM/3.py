import os
import re

def maketext(filename):
    with open(filename, encoding = 'cp1251') as f:
        text = f.read()
    return text

def findbigrams():
    pages = os.listdir('.')
    for page in pages:
        text = maketext(page)
        searchone = re.search(r'<meta content="(.*)?" name="docid"', text)
        if searchone:
            doc_id = searchone.groups()[0]
        else:
            print('что-то пошло не так')
        searchtwo = re.search(r'<meta content="(.*)?" name="topic"', text)
        if searchtwo:
            topic = searchtwo.groups()[0]
        else:
            print('и тут :(')
        bigrams = re.findall('gr="NUM.*?".*?</w><w>.*?gen', text)
        with open('three.csv', "w", encoding = 'cp1251') as f:
            for bigram in bigrams:
                f.write(doc_id)
                f.write(';')
                f.write(bigram)
                f.write(topic)
                f.write('\n')
    return

print('Тоже что-то непонятное - почему-то не хочет искать:')
findbigrams()
