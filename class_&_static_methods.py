# Methods of objects we've looked at so far are called by an instance of a class. However there are other type methods that a class can have - class and static methods
# Class methods are called on the class itself not on individual instances. This allow their use without needing to create a class instances. They are especially useful for actions relevant to the class as a whole rather than action limitied to a single object

class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

    def describe_book(self):
        print(self.title, 'by', self.author)

    @classmethod
    def books_in_series(cls,series_name,number_of_books):
        print("There are", number_of_books, "books in the", series_name, "series")

my_book = Book("Harry Potter and the sorcerer's stone","J.K.Rowling")
my_book.describe_book()
Book.books_in_series("Harry Potter", 7)

# Regular method :- Self
# class method :- cls

# To call a class method you dont need to create an instance of the class. Instead just use the class name, followed by a dot and the class method name

# Instance share everything that a class has, including the class methods. This mean that you call a class method on instance as well

# Static methods are similar to class method except they dont receive any additional arguments they are identical to normal functions that belongs to a class
# They are marked with the @staticmethod decorator

class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

    def describe_book(self):
        print(self.title, 'by' , self.author)

    @staticmethod
    def books_in_series(series_name, number_of_books):
        print("There are", number_of_books, 'books in the', series_name, 'series')

my_book = Book("Harry Potter & the sorcerers stone", "J.K.Rowling")
my_book.describe_book()
Book.books_in_series("Harry Potter", 7)

# When should you use the static methods instead of clss methods?
# Static methods dont accept the cls, parameter, meaning they can't access or modify the class state. They are useful when you require functionality that doesn't depend on the class behaviour or instance state and doesn't affect it. Essentially, static methods are suited for tasks that are self-contained and dont require knowledge of the class or isntance.
