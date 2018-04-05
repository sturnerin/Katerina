import re

def makehtml(filename):
    with open(filename, encoding = 'utf-8') as f:
        html = f.read()
    return html

def chaos(html):
    with open('chaos.txt', 'w', encoding = 'utf-8') as f:
        html = re.sub('Диноза́вры', 'Коты́', html)
        html = re.sub('Динозавр(?P<end>(а[мх]?)|(ами)|у|(о[мв])|е|ы|[^а-яА-Я])', 'Кот\g<end>', html)
        html = re.sub('динозавр(?P<end>(а[мх]?)|(ами)|у|(о[мв])|е|ы|[^а-яА-Я])', 'кот\g<end>', html)
        f.write(html)
    return

def run():
    html = makehtml('dino.html')
    chaos(html)
    return

run()
