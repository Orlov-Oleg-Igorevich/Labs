str_ = input("Введите целые числа: ")

if str_.isdigit():
    print(sum(list(map(int, str_))))
else:
    count = 0
    for i in str_:
        if i.isdigit():
            count += int(i)
    print(count)