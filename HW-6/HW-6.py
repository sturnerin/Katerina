import random
    
def noun():
    with open('noun.txt', encoding='utf-8') as f:
        text = f.read()
        a = text.split('\n')
        return random.choice(a)

def adverb():
    with open('adverb.txt', encoding='utf-8') as f:
        text = f.read()
        a = text.split('\n')
        return random.choice(a)

def neu():
    with open('neu.txt', encoding='utf-8') as f:
        text = f.read()
        a = text.split('\n')
        return random.choice(a)

def objectneu(neu):
    with open('neu_obj.txt', encoding='utf-8') as f:
        text = f.read()
        a = text.split('\n')
        random_neu = random.choice(a)
    result = neu + ' ' + random_neu
    return result

def verb_obj():
    with open('verb_obj.txt', encoding='utf-8') as f:
        text = f.read()
        a = text.split('\n')
        return random.choice(a)

def objectverb(verb_obj):
    with open('object.txt', encoding='utf-8') as f:
        text = f.read()
        a = text.split('\n')
    return verb_obj + ' ' + random.choice(a)

def verb():
    with open('verb.txt', encoding='utf-8') as f:
        text = f.read()
        a = text.split('\n')
        return random.choice(a)

def adverb_state():
    with open('verb_state.txt', encoding='utf-8') as f:
        text = f.read()
        a = text.split('\n')
        return random.choice(a)

def state(adverb_state):
    with open('state.txt', encoding='utf-8') as f:
        text = f.read()
        a = text.split('\n')
    return adverb_state + ' ' + random.choice(a)

def beg():
    with open('beg.txt', encoding='utf-8') as f:
        text = f.read()
        a = text.split('\n')
        return random.choice(a)

def link():
    with open('link.txt', encoding='utf-8') as f:
        text = f.read()
        a = text.split('\n')
        return random.choice(a)

def punct():
    with open('punct.txt', encoding='utf-8') as f:
        text = f.read()
        a = text.split('\n')
        return random.choice(a)

def part():
    with open('part.txt', encoding='utf-8') as f:
        text = f.read()
        a = text.split('\n')
        return random.choice(a)

def part_obj():
    with open('part_obj.txt', encoding='utf-8') as f:
        text = f.read()
        a = text.split('\n')
    return part() + ' ' + random.choice(a)

def sent1():
    return noun() + ' ' + adverb() + ' ' + verb() + ', ' + link() +\
        ' ' + noun() + ' ' + verb() + punct()

def sent2():
    return noun() + ' ' + adverb() + ' ' + objectverb(verb_obj())\
        + ', ' + link() + ' ' + noun() + ' ' + verb() + punct()

def sent3():
    return state(adverb_state()) + ', ' + verb() + ' ли ' + noun() + punct()

def sent4():
    return noun() + ' ' + objectverb(verb_obj()) + ', ' + link() + ' ' + noun()\
           + ' ' + verb() + punct()

def sent5():
    return objectneu(neu()) + ' ' + adverb() + ' ' + verb() + ', ' + link()\
           + ' ' + noun() + ' ' + adverb() + ' ' + verb() + punct()

def sent6():
    return noun() + ', ' + part_obj() + ', ' + verb() + ', ' + link()\
           + ' ' + noun() + ' ' + objectverb(verb_obj()) + punct()

def sent7():
    return beg() + ' ' + noun() + ' ' + objectverb(verb_obj()) + ', ' + noun()\
           + ', ' + part_obj() + ', ' + verb() + punct()

def random_sentence():
    version = random.randint(1, 7)
    if version == 1:
        return sent1()
    elif version == 2:
        return sent2()
    elif version == 3:
        return sent3()
    elif version == 4:
        return sent4()
    elif version == 5:
        return sent5()
    elif version == 6:
        return sent6()
    else:
        return sent7()

number = random.randint(5, 15)
for i in range(number):
    sentence = random_sentence()
    sentence = sentence.capitalize()
    print(sentence, end=' ')
