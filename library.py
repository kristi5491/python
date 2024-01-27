#Симулятор бібліотеки Створіть клас 'Бібліотека', який міститиме список книг (об'єкти класу 'Книга'). 
#Кожна книга має властивості: назва, автор, жанр.
# Реалізуйте методи для додавання книг, пошуку книги за назвою, видалення книги та виведення всіх книг певного жанру.



class Book:
    def __init__(self, title, author,year, genre):
        self.title = title
        self.author  = author
        self.year = year
        self.genre = genre
class Library:
    def __init__(self):
        self.book =[]

    def add_book(self, book):
        self.book.append(book)
        print(f'Книга {book} була успішно добавлена')

    # def search_by_name(self,book):



        