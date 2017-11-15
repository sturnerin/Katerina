a = input("введите слово: ")
i = len(a)-1
while i >= 0:
    print(a[i::])
    i -= 1
