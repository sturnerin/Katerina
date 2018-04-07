import re

def readfile():
    with open('mystem.xml', encoding = 'utf-8') as f:
        file = f.read()
    return file

def count(file):
    i = 0
    with open('count.txt', 'w', encoding = 'utf-8') as f:
        count = re.findall(r'<se>.*</se>?', file)
        for element in count:
            element = element.split('<se>\n')
            for line in element:
                i += 1
        f.write(str(i))
    return

def run():
    file = readfile()
    count(file)
    return

run()
