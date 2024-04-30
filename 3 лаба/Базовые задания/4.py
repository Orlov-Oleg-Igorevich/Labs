def positive():
    print("Положительное")

def negative():
    print("Отрицательное")

def test():
    N = int(input('Введите целое число: '))
    if N > 0: positive()
    elif N < 0: negative()

test()