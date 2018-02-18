import random
def makedict():
    with open('houses.csv', encoding = 'utf-8') as f:
        quiz = {}
        for line in f:
                word, a, b, c, d = line.split(';')
                helpword = quiz.setdefault(word, [])
                helpword.append(a)
                helpword.append(b)
                helpword.append(c)
                helpword.append(d.replace('\n', ''))
    return quiz

def playquiz(quiz):
    answer = random.choice(sorted(quiz.keys()))
    i = 0
    print('I am Hogwarts or Ilvermorny student. Can you guess my house? I am', random.choice(quiz[answer]), '...')
    trial = input().title()
    while trial != answer:
        if trial == '':
            trial = input('Hey, please try to guess :( ').title()
        else:
            print('No, I am', random.choice(quiz[answer]), '...')
            i += 1
            print('You have tried', i, 'time(s)! Keep guessing! ')
            trial = input().title()
    i += 1
    print('Hurrah! Well done!')
    print('All in all, you have tried', i, 'time(s).')
    print('Press Enter again to continue.')
    return

def run():
    button = input('Press Enter to start! ')
    while button == '':
        quiz = makedict()
        playquiz(quiz)
        button = input()
    print(':(')
    return

run()
