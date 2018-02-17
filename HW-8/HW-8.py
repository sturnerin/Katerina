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
    trial = input('I am Hogwarts or Ilvermorny student. Can you guess my house? ')
    while trial != answer:
        if trial == '':
            trial = input('Hey, please try to guess :( ')
        else:
            print('No, I am ', random.choice(quiz[answer]), '...')
            i += 1
            print('You have tried', i, 'time(s)! Keep guessing! ')
            trial = input()
    i += 1
    print('Hurrah! Well done!')
    print('All in all, you have tried', i, 'time(s).')
    return

def run():
    quiz = makedict()
    playquiz(quiz)

run()
