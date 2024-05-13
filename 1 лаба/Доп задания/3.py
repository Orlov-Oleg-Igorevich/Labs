x = int(input("Сколько чисел будет введено: "))
max_ = -10**10
min_ = 10**10

while x > 0:
    num = float(input("Введите число: "))
    if num > max_:
        max_ = num
    if num < min_:
        min_ = num
    x -= 1

print("Максимальное число:", max_)
print("Минимальное число:", min_)
