#Симулятор бібліотеки Створіть клас 'Бібліотека', який міститиме список книг (об'єкти класу 'Книга'). 
#Кожна книга має властивості: назва, автор, жанр.
# Реалізуйте методи для додавання книг, пошуку книги за назвою, видалення книги та виведення всіх книг певного жанру.

class Book:
    def __init__(self, title, author, year:int, genre):
        self.title = title
        self.author  = author
        self.year = year
        self.genre = genre
class Library:
    def __init__(self):
        self.books =[]

    def __print_book(self,book):
        print(f'title:{book.title} Author:{book.author} Year:{book.year} genre:{book.genre}\n ')

    def add_book(self, book):
        if book  not in self.books:
            self.books.append(book)
            print(f'Книга {book.title} була успішно добавлена')
        else:
            print(f'Книга {book.title} не була добавлена' )

    def search_by_name(self,search_title):
        found_books = []
        for book in self.books:
            if book.title.lower() == search_title.lower():
                found_books.append(book)
        for book in found_books:
            print('Ось книга за шуканим імям')
            self.__print_book(book)
    def delete_book(self, book ):
        if book in self.books:
           self.books.remove(book)
           print(f'Ми видвлили {book.title} з бібліотеки ')
        else:
            print(f' Вашу книгу не було знайдено')
    def search_by_genre(self, search_genre:str):
        found_books = []
        for book in self.books:
            if book.genre.lower() == search_genre.lower():
                found_books.append(book)
                for book in found_books:
                    print('Ось зеайдена книга за шуканим жанром')
                    self.__print_book(book)
            else:
                print('Ми не змогли найти цього жанру в бібліотеці')
        return found_books      
           
library = Library()
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Fiction")
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction")
book3 = Book("1984", "George Orwell", 1949, "Dystopian Fiction")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.search_by_name('The Great Gatsby')
library.search_by_genre('Dystopian Fiction')
library.delete_book(book2)






        