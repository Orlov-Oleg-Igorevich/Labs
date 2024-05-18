import numpy as np

def table(a, b, n):
    max_null_line = -1
    max_null = -1
    for line in range(n):
        if np.count_nonzero (a[line] == 0) > max_null:
            max_null = np.count_nonzero (a[line] == 0)
            max_null_line = line

    max_sum_line = -1
    max_sum = -1
    for line in range(n):
        if sum(b[line]) > max_sum:
            max_sum = sum(b[line])
            max_sum_line = line

    t1, t2, t3, t4 = [[] for i in range(max_null_line)], [[] for i in range(max_null_line)], [[] for i in range(max_null_line, n-1)], [[] for i in range(max_null_line, n-1)]
    for i in range(n):
        for j in range(n):
            if i < max_null_line and j < max_sum_line:
                t1[i].append(a[i][j])
            if i < max_null_line and j > max_sum_line:  
                t2[i].append(a[i][j])
            if i > max_null_line and j < max_sum_line:
                t3[i-1 - max_null_line].append(a[i][j])
            if i > max_null_line and j > max_sum_line:
                t4[i-1 -max_null_line].append(a[i][j])
    return t1, t2, t3, t4

print("Входные данные: ")
a = np.random.randint(-3, 3, size = (5, 5))
b = np.transpose(a)
print(a)
print()
count = 0
print('Результат: ')
for i in table(a, b, 5):
    count += 1
    print(f"Таблица номер {count}: ")
    print(np.asarray(i))