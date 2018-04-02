import re

def openfile(filename):
    with open(filename, encoding = 'utf-8') as f:
        html = f.read()
    return html

def searchinfo(html):
    info = re.search('(Семейство:)&#160;</td><td.*?><a.*?>(.*?)</a>', html)
    if info:
        print(info.groups()[0], info.groups()[1])
    else:
        print('Я ничего не нашел, извините!')
    return

def run():
    html = openfile('lan.html')
    searchinfo(html)
    return

run()
