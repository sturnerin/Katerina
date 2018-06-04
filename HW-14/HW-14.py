def readtale(filename):
    with open(filename, encoding = "utf-8") as f:
        baretale = f.read()
    tale = baretale.replace(',', '')
    tale = tale.replace('«', '')
    tale = tale.replace('»', '')
    tale = tale.replace('»', '')
    tale = tale.replace('—', '')
    tale = tale.replace(':', '')
    tale = tale.replace(';', '')
    tale = tale.replace('!', '')
    tale = tale.replace('?', '')
    tale = tale.replace('…', '')
    tale = tale.replace('.', '')
    tale = tale.split()
    return tale

def doathing(tale):
    for word in tale:
        chars = {c: word.count(c) for c in word}
        for c in word:
            c.replace(c, c*chars[c])    
    return

def run():
    # tale = readtale('chudovishe.txt')
    # doathing(tale)
    # for w in tale:
        # print(w, end=' ')
    print('Это не работает, но я пыталась :(')
    return

run()
