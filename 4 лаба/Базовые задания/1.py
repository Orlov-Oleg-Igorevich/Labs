a, b = input('Введите первое значение: '), input('Введите второе значение: ')

try:
    a, b = int(a), int(b)
    print(f'Результат сложения чисел {a} и {b}: {a+b}')
except ValueError:
    print(f'Результат конкатенации строк: {a+b}')