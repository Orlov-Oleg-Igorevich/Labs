#каждому из гостей достался хотя бы 1 кусок
n = int(input('Введите количество гостей: '))

piece = 1
cut = 0
while piece < n:
    cut += 1
    piece += 1

print(cut)

#как минимум половине гостей досталось по 2 куска
n = int(input('Введите количество гостей: '))

piece = 1
cut = 0
while piece < n*2:
    cut += 1
    piece += 1

print(cut)

#каждому гостю досталось по 1 куску и при этом ещё хотя бы 10 кусков осталось в запасе
n = int(input('Введите количество гостей: '))

piece = 1
cut = 0
while piece - 10 < n:
    cut += 1
    piece += 1

print(cut)
