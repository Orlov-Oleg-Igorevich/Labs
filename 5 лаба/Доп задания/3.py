N = int(input('Введите количество чисел: '))
number_2, number_13, number_26 = 0, 0, 0


for i in range(1, N + 1):
    number = int(input(f'Введите число номер {i}: '))
    if number % 2 == 0:
        number_2 += 1
    if number % 13 == 0:
        number_13 += 1
    if number % 26 == 0:
        number_26 += 1


pairs_26 = number_26 * (N - number_26) + number_26 * (number_26 - 1) // 2

pairs_2_13 = number_2 * number_13

total_pairs = pairs_26 + pairs_2_13

print(f'На 26 делится произведение {total_pairs} пар чисел')