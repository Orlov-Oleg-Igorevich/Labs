def SiftDown(list_, i, n):
    nMax = i
    value = list_[i][-2]
    value2 = list_[i]
    while True:
        i = nMax
        childN = i*2 + 1
        if childN < n and list_[childN][-2] > value:
            nMax = childN
        childN += 1
        if childN < n and list_[childN][-2] > list_[nMax][-2]:
            nMax = childN
        if nMax == i:
            break
        list_[i] = list_[nMax]
        list_[nMax] = value2

def HeapSort(list_, n):
    for i in range(n//2-1, -1, -1):
        SiftDown(list_, i, n)
    while n > 1:
        n -= 1
        list_[0], list_[n] = list_[n], list_[0]
        SiftDown(list_, 0, n)
    return list_

with open('MPCORB.DAT.txt') as f:
    a = [i for i in f.readlines() if i]
    s = [i.split() for i in a]

d = [i for i in s if i]

c = HeapSort(d, len(d)) #отсортиованный список

def binary_search(list_, key):
    low = 0
    high = len(list_) - 1

    while low <= high:
        mid = (low + high) // 2
        midVal = list_[mid][-2]
        if midVal == key:
            return mid
        if midVal > key:
            high = mid - 1
        else:
            low = mid + 1
    return 'Не найдено'

c[binary_search(c, 'AA')]

def search(list_, key):
    count = 0
    value = list_[0][-2]
    while key != value:
        count += 1
        value = list_[count][-2]
    return count

c[search(c, 'AA')]