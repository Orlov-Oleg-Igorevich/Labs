n, m = int(input("Введите количество детей: ")), int(input("Введите количество кубиков: "))

count = 1
num = 1
while count <= m:
    m -= count
    count *= 2
    if count > 25:
        count -= 25
    num += 1
    if num > n:
        num = 1

print(f'Проигравшим будет {num} ребёнок')