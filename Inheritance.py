class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

dog = Dog()
dog.speak()
dog.bark()

class Animal:
    def speak(self):
        print("Animal speaks")

class Bird:
    def fly(self):
        print("Bird flies")

class Bat(Animal, Bird):
    def sound(self):
        print("Bat makes a sound")

bat = Bat()
bat.speak()
bat.fly()
bat.sound()

class Animal:
    def eat(self):
        print("Animal eats")

class Mammal(Animal):
    def walk(self):
        print("Mammal walks")

class Dog(Mammal):
    def bark(self):
        print("Dog barks")

dog = Dog()
dog.eat()
dog.walk()
dog.bark()
