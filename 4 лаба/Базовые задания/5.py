#на основе рекурсии

def move(n, x, y):

    if x+y == 3:
        z = 3
    elif x+y == 5:
        z = 1
    else:
        z = 2

    if n == 1:
        return print(f'Переместить {n} диск на {y} пирамидку')
    else:
        move(n-1, x, z)
        print(f'Переместить {n} диск на {y} пирамидку')
        move(n-1, z, y)

#n, x, y = int(input("Введите количество дисков: ")), int(input("С какой пирамидки передвинуть(укажите номер пирамидки: 1, 2, 3): ")), int(input("На какую пирамидку передвинуть(укажите номер пирамидки: 1, 2, 3): "))
n, x, y = 3, 1, 2
print('Порядок действий: ')
move(n, x, y)   

#на основе цикла
n =  3
a = []
def f(k, n):
    if n % 2 == 0 and k % 2 == 0 or n % 2 != 0 and k % 2 != 0:
        x, y, z = 1, 2, 3
    else:
        x, y, z = 1, 3, 2

    for i in range(2**k - 1, 2**n - 1, 2**(k + 1)):
        a[i].append(k + 1)
        a[i].append(x)
        a[i].append(y)
        x, y, z = y, z, x


for i in range(2**n - 1):
    a.append([])

for i in range(n):
    f(i, n)

for i in range(len(a)):
    print('Диск ', a[i][0], ' : ' , a[i][1], ' =====> ', a[i][2])
