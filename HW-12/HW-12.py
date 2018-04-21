import os, re

def count():
    i = 0
    names = []
    for filename in os.listdir():
        path = './' + filename
        if os.path.isdir(path):
            barepath, barename = os.path.split(path)
            m = re.search('.*[a-zA-zа-яА-я].* .*[a-zA-zа-яА-я].*', filename)
            if m:
                i += 1
                names.append(barename)
    print('папок - ', i)
    print ('нашлись: ')
    for name in names:
        print(name, end = '\n')
    return

count()
