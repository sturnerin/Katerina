import os, re

def count():
    i = 0
    names = []
    for root, dirs, files in os.walk("."):
        for f in files:
            name = re.sub('\..*', '', f)
            if name not in names:
                names.append(name)
                i += 1
    return i

def run():
    i = count()
    print('Разных названий файлов - ', i)
    return

run()
