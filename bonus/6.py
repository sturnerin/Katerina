height = int(input('Какой у вас рост? (см) '))
weight = int(input('Какой у вас вес? (кг) '))
heightinm = height/100
index = weight/(heightinm**2)
if index <= 16:
    print('Интерпретация показателя ИМТ - выраженный дефицит массы тела.')
if index > 16 and index <= 18.5:
    print('Интерпретация показателя ИМТ - недостаточная масса тела (дефицит).')
if index > 18.5 and index <= 24.99:
    print('Интерпретация показателя ИМТ - норма.')
if index >= 25 and index < 30:
    print('Интерпретация показателя ИМТ - избыточная масса тела (предожирение).')
if index >= 30 and index < 35:
    print('Интерпретация показателя ИМТ - ожирение первой степени.')
if index >= 35 and index < 40:
    print('Интерпретация показателя ИМТ - ожирение второй степени.')
if index >= 40:
    print('Интерпретация показателя ИМТ - ожирение третьей степени (морбидное).')