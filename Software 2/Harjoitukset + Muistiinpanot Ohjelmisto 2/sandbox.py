class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("Eläin ääntelee!")

    def introduction(self):
        print(f"Tämän eläimen nimi on {self.name} ja ikä {self.age}.")

class Cat(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def meow(self):
        print("Meow!")

    def introduction(self):
        super().introduction()
        print(f"Rodultaan {self.breed}.")


animal1 = Animal("Bob", 20)
animal1.speak()
animal1.introduction()

cat1 = Cat("Onni", 6, "Siamese")
cat1.meow()
cat1.introduction()

animals = []
animals.append(cat1)
animals.append(animal1)

for a in animals:
    a.speak()




