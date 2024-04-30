n = input('Введите четырёхзначное число: ')

while len(n) < 4:
    n = '0' + n


if n[:2] == n[2:][::-1]:
    print(1)
else:
    print(100)
