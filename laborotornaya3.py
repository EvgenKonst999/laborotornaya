#Задание 1
class Book:
    def __init__(self, title, author, age):
        self.title = title
        self.author = author
        self.age = age
    def get_info (self):
        return {'Название книги': self.title, 'Автор': self.author, 'Год издания': self.age}
book_1 = Book('Мертвые души', 'Николай Гоголь', 1835) #Пример
print(book_1.get_info())




#Задание 2
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def get_radius (self):
        return self.radius
    def set_radius(self, new_radius):
        self.radius = new_radius
circle_1 = Circle(2) #Пример
print({circle_1.get_radius()})
circle_1.set_radius(10)
print({circle_1.get_radius()})