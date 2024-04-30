import json

info = [
    {
    "имя":"Иван",
    "телефоны":[
       {
          "описание":"прапрпа",
          "номер":"33"
       },
       {
          "описание":"рпыврп",
          "номер":"45"
       }
    ]
    }
]
with open('PhoneDirectory.json', "w") as fh:
    fh.write(json.dumps(info, ensure_ascii=False, indent=4))



try:
    file = open("PhoneDirectory.json", 'r')
    print("Файл успешно открыт!")
except FileNotFoundError:
    # Обработка ошибки, возникающей в том случае, если файл не найден
    print("Файл не найден!")
    exit()
except PermissionError:
    # Обработка ошибок, связанных с разрешением на доступ к файлу
    print("Ошибка доступа!")
else:
    data = json.loads(file.read())
    print("Информация загружена")
    
# Прибираемся после себя даже в том случае, если выше возникло исключение
finally:
    file.close()

ans = int(input('''Что вы хотите сделать?(введите номер варианта): 
    1. выполнять поиск контактов по номеру телефона;
    2. выполнять поиск контактов по имени;
    3. добавить контакт по имени;
    4. удалять контакты по имени;
    5. удалять номер телефона из контактов по имени;
    6. сохранять справочник с изменениями в файл и закончить рабочую сессию
    7. показать изменённый справочний
    8. прервать сессию'''))


while True:

    if ans == 1:
        telephone = input("Введите номер телефона: ")
        found = False
        for i in data:
            for contact in i['телефоны']:
                if telephone == contact['номер']:
                    found = True
                    print(f'Контакты {i['имя']}: ')
                    for contact in i['телефоны']:
                        print(contact['номер'])
                    print("Действие выполнено!")
            if found: break
                
    if ans == 2:
        name = input("Введите имя человека, чьи контакты необходимо найти: ")
        for i in data:
            if name == i['имя']:
                print(f'Контакты {i['имя']}: ')
                for contact in i['телефоны']:
                    print(contact['номер'])
                print("Действие выполнено!")
                break

    if ans == 3:
        name = input("Введите имя человека, которому необходимо добавить контакт: ")
        description = input("Введите описание контакта: ")
        number = input("Введите номер контакта: ")
        for i in data:
            if name == i['имя']:
                i['телефоны'].append({'описание': description, 'номер': number})
                print("Действие выполнено!")
                break

    if ans == 4:
        name = input("Введите имя человека, которому необходимо удалить контакты: ")
        for i in data:
            if name == i['имя']:
                i['телефоны'] = []
                print("Действие выполнено!")
                break

    if ans == 5:
        name = input("Введите имя человека, которому необходимо удалить номер: ")
        telephone = input("Введите номер, который необходимо удалить: ")
        found = False
        for i in data:
            if name == i['имя']:
                found = True
                for contact in range(len(i['телефоны'])):
                    if telephone == i['телефоны'][contact]['номер']:
                        i['телефоны'].remove(i['телефоны'][contact])
                    print("Действие выполнено!")
            if found: break

    if ans == 6:
        with open("NewPhoneDirectory.json", 'w') as f:
            f.write(json.dumps(data, ensure_ascii=False, indent=4))
        break

    if ans == 7:
        print(data)
    
    if ans == 8:
        break


    ans = int(input('''Что вы хотите сделать?(введите номер варианта): 
    1. выполнять поиск контактов по номеру телефона;
    2. выполнять поиск контактов по имени;
    3. добавить контакт по имени;
    4. удалять контакты по имени;
    5. удалять номер телефона из контактов по имени;
    6. сохранять справочник с изменениями в файл и закончить рабочую сессию
    7. показать изменённый справочний
    8. прервать сессию'''))
print(data)