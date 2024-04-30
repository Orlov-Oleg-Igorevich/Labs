def arv(num: list):
    return sum(num)/len(num)
list_ = [1, 2, 3, 4, 5]
print("Среднее значение этих 5 чисел равно %.5f" % (arv(list_)))
x = float(input("Добавьте ещё число: "))
while x:
    list_.append(x)
    print("Среднее значение этих %.i чисел равно %.5f" % (len(list_), arv(list_)))
    x = float(input())