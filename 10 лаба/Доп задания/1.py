def SiftDown(list_, i, n):
    nMax = i
    value = list_[i]
    while True:
        i = nMax
        childN = i*2 + 1
        if childN < n and list_[childN] > value:
            nMax = childN
        childN += 1
        if childN < n and list_[childN] > list_[nMax]:
            nMax = childN
        if nMax == i:
            break
        list_[i] = list_[nMax]
        list_[nMax] = value

def HeapSort(list_, n):
    for i in range(n//2-1, -1, -1):
        SiftDown(list_, i, n)
    while n > 1:
        n -= 1
        list_[0], list_[n] = list_[n], list_[0]
        SiftDown(list_, 0, n)
    return list_

ary = [0,3,5,1,2,3,5,4,2,34,43,24]
print(HeapSort(ary, len(ary)))