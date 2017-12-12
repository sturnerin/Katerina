m = 0
wordlist = []
a = input("пожалуйста, вводите названия языков ")
while a != "":
    wordlist.append(a)
    a = input()
with open("lang.tsv", encoding="utf-8") as f:
    lines = f.readlines()
    for word in wordlist:
        for line in lines:
            line = line.split('\t')
            if word == line[0]:
                print(line[0], "-", line[1], "-", line[2])
                m = 1
                break
        if m == 0:
            print("языка", word, "нет в списке\n")
        m = 0
