import matplotlib.pyplot as plt


school = {'1а': 24, '1б': 27, '2б': 19, '3a': 33, '4a': 22, '4б': 20, '6а': 15, '7в': 28}

def change():

    n = input('''Изменения какого типа вы хотите внести?(укажите букву):
    a) в одном из классов изменилось количество учащихся; 
    b) в школе появился новый класс; 
    c) в школе был расформирован (удален) класс, в связи с чем ученики были равномерно распределены по другим; 
    d) выгрузка данных: общее количество учащихся в школе, общее количество классов, распределение учеников по классам''')

    if n == 'a':
        name = input('В какой класс необходимо внести изменения?: ')
        n = int(input("Введите актуальное колличество участников: "))
        school[name] = n

    elif n == 'b':
        name = input('Введите наименование нового класса: ')
        n = int(input("Введите актуальное количество участников: "))
        school[name] = n
    elif n == 'c':
        name = input('Введите наименование расформированного класса: ')
        value = school.pop(name)
        for i in school:
            if school[i] == min(school.values()):
                school[i] += value//len(school) + value%len(school)
            else:
                school[i] += value//len(school)
    elif n == 'd':
        n = sum(school.values())
        print(f'Общее количество учащихся: {n}')
        col = len(school.keys())
        print(f'Общее количество классов: {col}')
        index = school.keys()
        values = school.values()
        plt.title('Распределение учеников по классам')
        plt.bar(index,values)
        plt.show()


change()
