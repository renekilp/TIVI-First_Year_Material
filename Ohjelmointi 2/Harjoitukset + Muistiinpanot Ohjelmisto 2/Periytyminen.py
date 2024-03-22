class Animal:
    def __init__(self, species):
        self.species = species

    def speak(self):
        print("Animal is making a sound!")


class Dog(Animal):
    def __init__(self, species, breed):
        super().__init__(species)
        self.breed = breed

    def speak(self):
        print("Dog is making a sound!")


animal1 = Animal("Dog")
dog1 = Dog("Dog", "Shiba Inu")
dog1.speak()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        print(f"Hi! My name is {self.name}. I'm {self.age} years old.")


class Student(Person):
    def __init__(self, name, age, student_number):
        super().__init__(name, age)
        self.student_number = student_number

    def greeting(self):
        super().greeting()
        print(f"My student number is {self.student_number}.")


person1 = Person("Maya", 21)
student1 = Student("Bob", 22, 123456)


student1.greeting()
