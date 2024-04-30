def binary_search(list_, key):
    low = 0
    high = len(list_) - 1

    while low <= high:
        mid = (low + high) // 2
        midVal = list_[mid]
        if midVal == key:
            return mid
        if midVal > key:
            high = mid - 1
        else:
            low = mid + 1
    return 'Не найдено'


def gold_search(list_, key):
    a = 0
    b = len(list_) - 1
    while a <= b:
        x1 = int(b - (b-a)/1.618)
        x2 = int(a + (b-a)/1.618)
        y1 = list_[x1]
        y2 = list_[x2]
        if y1 == key:
            return x1
        elif y2 == key:
            return x2
        elif y1 < key:
            a = x1
        else:
            b = x2


def interpolation_search(list_, key):
    low = 0
    high = len(list_) - 1

    while low <= high  and list_[high] > key:
        if list_[high] == list[low]:
            return ("Всё плохо")
        mid = low + ((key - list_[low])*(high - low))//(list_[high] - list_[low])
        midVal = list_[mid]
        if midVal == key:
            return mid
        if midVal > key:
            high = mid - 1
        else:
            low = mid + 1
    if list_[low] == key:
        return low
    if list_[high] == key:
        return high

    return "Ничего не найдено"


ary = [0, 1, 2, 2, 3, 3, 4, 5, 5, 24, 34, 43]

print(binary_search(ary, 5))
print(gold_search(ary, 5))
print(interpolation_search(ary, 5))