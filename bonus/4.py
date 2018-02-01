text = str(input('Что сказать? '))
vowelsdown = 'аеёиоуыэюя'
vowelsup = 'АЕЁИОУЫЭЮЯ'
uptodown = {'А': 'а', 'Е': 'е', 'Ё': 'ё', 'И': 'и', 'О': 'о', \
            'У': 'у', 'Ы': 'ы', 'Э': 'э', 'Ю': 'ю', 'Я': 'я'}
hogwash = ''
for letter in text:
    if letter in vowelsdown:
        hogwash = hogwash + letter + 'с' + letter
        continue
    if letter in vowelsup:
        for key, value in uptodown.items():
            if letter == key:
                hogwash = hogwash + letter + 'с' + value
    else:
        hogwash = hogwash + letter
print(hogwash)
