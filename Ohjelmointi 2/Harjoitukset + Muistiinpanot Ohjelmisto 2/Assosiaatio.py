class School:
    def __init__(self, name):
        self.name = name


class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school


school1 = School("Lykki")
school2 = School("Karamalmin kampus")
student1 = Student("Eemil", school1)
student2 = Student("Patrik", school2)

print(f"{student1.name} is studying @ {student1.school.name}")
print(f"{student2.name} is studying @ {student2.school.name}")


class Book:
    def __init__(self, title):
        self.title = title


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)


book1 = Book("The legend of Onni")
book2 = Book("Eemilin vitsit")
book3 = Book("Jonin ponien kasvatuksen salat")

library1 = Library("Salaiset romaanit")
library2 = Library("Hupaisat kertomukset")

library1.add_book(book1)
library1.add_book(book3)
library2.add_book(book2)

print(f"{library1.name} kuuluvat kirjat:")
for book in library1.books:
    print(book.title)




