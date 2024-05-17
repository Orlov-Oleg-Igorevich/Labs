def search2(list1, list2):
    count = 0
    for i in list2:
        while i != list1[count]:
            count += 1
            if count > len(list1)-1:
                return 'Не является'
    else:
        return 'Является'

search2([1, 2, 3, 4, 5, 6], [2, 6])