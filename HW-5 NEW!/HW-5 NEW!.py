ru=list('ДЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮёйцукенгшщзхъфывапролджэячсмитьбю')
with open("latinwords.txt", "a", encoding="utf-8") as f:
    print("пожалуйста, вводите латинские слова, пока вам не надоест ")
    a=input()
    alist=list(a)
    lena=len(a)
    lenru=len(ru)
    for i in range(lena):
        for j in range(lenru):
            if alist[i]==ru[j]:
                print("а латынь кириллицей не пишут")
    if a=="":
        print("вы ничего не ввели :(")
    else:
        while a!="":
            if a.endswith("tur"):
                f.write(a)
                f.write("\n")
            a=input()
