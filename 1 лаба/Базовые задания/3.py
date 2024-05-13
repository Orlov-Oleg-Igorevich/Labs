sum_ = 1+2+3+4+5
count = 5
arv = sum_/count
print("Среднее значение этих 5 чисел равно %.5f" % (arv))
x = float(input("Добавьте ещё число: "))
while x:
    sum_ += x
    count += 1
    arv = sum_/count
    print("Среднее значение этих %.i чисел равно %.5f" % (count, arv))
    x = float(input())
