class library:

    def __init__(self):
        
        self.books = []

    class book:

        def __init__(self, name, year, author, tags=[]):

            self.name = name
            self.year_of_publication = year
            self.author = author
            self.tags = [] + tags

        def __str__(self):
                return self.name

    def append(self, other): #– для добавление книги
        try:
                if all(other[0] != i.name for i in self.books):
                        return self.books.append(library.book(*other))
                else: print('Книга уже существует')
        except:
                print('''Ведите книгу в следующем формате: ожидается список, где первый элемент - название,
                второй - год издания, третий - автор, четвёртый - список тегов''')

    def search(self, other): #– для поиска книги
        for book in self.books:
                if any(other == i for i in [book.name, book.year_of_publication, 
                book.author]) or other in book.tags:
                        return f'''Название книги - {book.name}, год издания - {book.year_of_publication}, автор - {book.author}, теги: {', '.join(book.tags)}.'''
                else: return 'Книга не найдена'


    def removal(self, other): #– для удаления книги
        for i in self.books:
            if other == i.name:
                self.books.remove(i)

    def sorting(self): #– для сортировки книг
        ans = int(input('''Как хотите отсортировать?(введите цифру):
        1) По году издания
        2) По автору
        3) По названию'''))
        if ans == 1:
                self.books.sort(key = lambda x: x.year_of_publication)

        if ans == 2:
                self.books.sort(key = lambda x: x.author)

        if ans == 3:
                self.books.sort(key = lambda x: x.name)

    def __str__(self):
        a = [i.name for i in self.books]
        return str(a)


lib1 = library()
lib1.append(["Война и мир", 1884, 'Л.Н. Толстой', ['война', "поиск себе"]])
lib1.append(["Преступление и наказание", 1874, 'Ф.М. Достоевский', ['убийство', "муки"]])
print(lib1.search('Л.Н. Толстой'))
print(lib1.search('война'))
print(lib1)
lib1.sorting()
print(lib1)