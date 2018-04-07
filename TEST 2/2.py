import re

def readfile():
    with open('mystem.xml', encoding = 'utf-8') as f:
        file = f.read()
    return file

def makedict(file):
    m = re.findall('<w>.*</w>?', file)
    for thing in m:
        thing = re.sub('<w>.*?gr="(?P<gram>.*)?".*?</w>?', r'\g<gram>', thing)
    adict = {}
    for element in m:
        if element in adict:
            adict[element] += 1
        else:
            adict[element] = 1
    return adict

def writefile(adict):
    with open('dict.txt', 'w', encoding = 'utf-8') as f:
        for key in sorted(adict):
            couple1 = str(key)
            couple2 = str(adict[key])
            f.write(couple1)
            f.write(' : ')
            f.write(couple2)
            f.write('\n')
    return

def run():
    file = readfile()
    adict = makedict(file)
    writefile(adict)
    return

run()
