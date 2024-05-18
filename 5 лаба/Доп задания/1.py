def dict_super(dict_):

    d = {}
    for i, j in dict_:
        for k in j:
            d[k] = []

    for i, j in dict_:
        for k in j:
            d[k].append(str(i))

    for i in d:
        d[i] = int(''.join(d[i]))
    return d

a = {1: 'acc', 2: 'cab', 3: 'ccb'}
print(f'Исходный словарь: ')
c = dict_super(a.items())
print(f'Выходной словарь2: {c}')