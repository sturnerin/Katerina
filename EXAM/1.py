import os
import re

def maketext(filename):
    with open(filename, encoding = 'cp1251') as f:
        text = f.read()
    return text

def cleantext(text):
    search = re.search(r'<title>(.*)?<title>?', text)
    if search:
        title = search.groups()[0]
    else:
        print('... :(')
    textlist = re.findall('</ana>.*?</w>?', text)
    for word in textlist:
        word.replace('</ana>', '')
        word.replace('</w>', '')
        word.replace('`', '')
    return textlist, title

def doathing():
    print('Мне кажется, что код похож на правду, но в чем ошибка, я не понимаю')
    pages = os.listdir('.')
    for page in pages:
        if page.endswith('html'):
            text = maketext(page)
            textlist, title = cleantext(text)
            newfile = page.replace('html', 'txt')
            with open(newfile, "w", encoding = 'cp1251') as f:
                f.write(title)
                f.write('\n')
                for word in textlist:
                    f.write(word)
                    f.write(' ')
    return

doathing()
