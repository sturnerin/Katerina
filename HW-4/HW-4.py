with open("text.txt", encoding = "utf-8") as f:
    text = f.read()
text = text.replace(' —', '')
text = text.replace('.', '')
text = text.replace(',', '')
text = text.replace('«', '')
text = text.replace('»', '')
text = text.replace('?', '')
text = text.replace('!', '')
text = text.replace(';', '')

splited_text = text.split()

n = 0
for word in splited_text:
    if len(word) > 10:
        n += 1
m = (n/len(splited_text))*100
print(m,"%")

