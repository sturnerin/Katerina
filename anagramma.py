import random

def anno(word):
    a = random.sample(word, len(word))
    newword = ''.join(a)
    return newword

with open('text.txt', encoding = 'utf-8') as f:
          text = f.read()
text = text[1:]
text = text.replace(',', '')
text = text.replace('.', '') 
words = text.split()
print(words)

with open('table.csv', 'w') as f:
    for x in words:
        listline = [x]
        for i in range(3):
            listline.append(anno(x))
        line = ';'.join(listline)
        f.write(line)
        f.write('\n')
