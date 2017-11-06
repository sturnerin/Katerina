a = input('write a word ')
h = len(a)//2
if len(a) == 1:
    print(a)
else:
    print(a[0:h])
    print(a[:h-1:-1])
