str_ = input('Введите строку: ')

count_upper = 0
count_lower = 0
for i in str_:
    if i.isupper():
        count_upper += 1
    if i.islower():
        count_lower += 1

if count_upper > count_lower:
    print(str_.lower())
elif count_upper < count_lower:
    print(str_.upper())
else:
    print(str_)