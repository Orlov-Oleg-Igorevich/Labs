n = input('Введите целое число: ')

if n[-2:] in set(i for i in range(11, 20)):
    print(f'На лугу пасётся {n} коров')
elif n[-1] == '1':
    print(f'На лугу пасётся {n} корова')
elif n[-1] in '234':
    print(f'На лугу пасётся {n} коровы')
else:
    print(f'На лугу пасётся {n} коров')
