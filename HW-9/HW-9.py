import re
def maketext():
    with open('всеформы.txt', encoding='utf-8') as f:
        words = f.read()
    words = words.replace(',', '')
    words = words.replace('!', '')
    words = words.replace('.', '')
    words = words.replace('?', '')
    return words

def findthem(words):
    eat = []
    eat1 = re.findall('съе(?:вше|денно)(?:го|му)\s', words)
    carryon(eat, eat1)
    eat2 = re.findall('съесть?\s', words) 
    carryon(eat, eat2)
    eat3 = re.findall('съел[аио]?\s', words) 
    carryon(eat, eat3)
    eat4 = re.findall('съе(?:шь|шьте)\s', words) 
    carryon(eat, eat4)
    eat5 = re.findall('съеденн[оы][ейм]\s', words) 
    carryon(eat, eat5)
    eat6 = re.findall('съеден[аоы]?\s', words) 
    carryon(eat, eat6)
    eat7 = re.findall('съевш[еи][ейм]\s', words) 
    carryon(eat, eat7)
    eat8 = re.findall('съед(?:им|ите|ят)\s', words) 
    carryon(eat, eat8)
    eat10 = re.findall('съе[в(?:дят)м]\s', words) 
    carryon(eat, eat10)
    eat11 = re.findall('съевш(?:ая|ую|их|ими)\s', words) 
    carryon(eat, eat11)
    eat12 = re.findall('съеденн(?:ая|ую|ых|ыми)\s', words) 
    carryon(eat, eat12)
    return eat

def exactword(k, anylist):
    tinylist = []
    for word in anylist:
        if word == k:
            tinylist.append(word)
    return tinylist

def carryon(l, m):
    if m:
        l.append(m)
    else:
        m = ''
    return

def run():
    n = 0
    words = maketext()
    eat = findthem(words)
    for eachlist in eat:
        for word in eachlist:
            print(word, end = '\n')
            n += 1
    print(n)
    return

run()

