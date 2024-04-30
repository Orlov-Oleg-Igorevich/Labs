try:
    x = int(input("Сколько чисел будет введено: "))
    num = [float(input("Введите число: ")) for i in range(x)]
    print("Максимальное число:", max(num))
    print("Минимальное число:", min(num))
except:
    print("Проверьте корректность ввода")