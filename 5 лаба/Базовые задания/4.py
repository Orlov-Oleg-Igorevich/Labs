def dict_magic(dict_):

    d = {}
    for i, j in dict_:
        d[j] = i
    return d

def dict_super(dict_):

    d = {}
    for i, j in dict_:
        for k in j:
            d[k] = []

    for i, j in dict_:
        for k in j:
            d[k].append(i)

    for i in d:
        d[i] = d[i]
    return d

a = {1: 'acc', 2: 'cab', 3: 'ccb'}
print(f'Исходный словарь: ')
b = dict_magic(a.items())
print(f'Выходной словарь1: {b}')
c = dict_super(a.items())
print(f'Выходной словарь2: {c}')