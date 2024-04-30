with open("ИмяФайла.txt") as f1:
    a = f1.read()
    with open("Copy ИмяФайла.txt", 'w') as f2:
        f2.write(a)
