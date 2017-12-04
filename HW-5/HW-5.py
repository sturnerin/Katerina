with open("latinwords.txt", "a", encoding="utf-8") as f:
    print("пожалуйста, вводите латинские слова, пока вам не надоест ")
    a=input()
    if a=="":
        print("вы ничего не ввели :(")
    else:
        while a!="":
            if a.endswith("tur"):
                f.write(a)
                f.write("\n")
            a=input()
