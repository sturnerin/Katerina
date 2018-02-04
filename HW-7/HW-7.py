def listone():
    filename = input('введите название файла: ')
    with open(filename, encoding='utf-8') as f:
        text = f.read()
    text = text.replace(' - ', ' ')
    text = text.replace('-', '')
    text = text.replace(', ', ' ')
    text = text.replace('. ', ' ')
    text = text.replace(': ', ' ')
    text = text.replace('; ', ' ')
    text = text.lower()
    words = text.split()
    return words

def listwo(words):
    num = 0
    length = 0
    for word in words:
        if word.endswith('ous'):
            length += len(word)
            num += 1
    return length, num

def count(words, length, num):
    average = length // num
    print('прилагательных - ', num)
    print('средняя длина - ', average)
    return

def run():
    words = listone()
    length, num = listwo(words)
    count(words, length, num)
    return

run()
