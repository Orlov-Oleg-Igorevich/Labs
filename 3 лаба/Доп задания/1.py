countTrue = 0
countFalse = 0

while countTrue < 5:
    a, b = int(input("Введите первое однозначное число: ")), int(input("Введите второе однозначное число: "))
    ans = int(input(f'Результат умножения {a} на {b} равен?: '))
    if ans == a*b:
        print('Правильный ответ!')
        countTrue += 1
        if countTrue == 3:
            print("Молодец! Три правильных ответа!")
    else:
        countFalse += 1
        print(f'Неправильный ответ! Верный ответ: {a*b}')
        if countFalse == 3:
            print('Ты плохой')