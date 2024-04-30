a = []
with open("Кинозал.txt") as f:
    for i in f:
        a.append(list(map(int, i.split())))

free_row = 0
count = 0
rows = []
for i in a:
    for j in i:
        count += 1
        if j == 0:
            free_row += 1
    rows.append(free_row)
    free_row = 0

print(f'Всего мест в зале: {count}')
print(f'Из них свободных: {sum(rows)}')
for i in range(len(rows)):
    print(f'{i+1} ряд - свободных мест: {rows[i]}')


row = int(input(f"Какой ряд хотите проверить?(всего рядов - {len(rows)}): "))
place = int(input(f"Какой место хотите проверить?(всего мест - {len(a[row-1])}): "))
print("Место свободно" if a[row-1][place-1] == 0 else "Место занято")