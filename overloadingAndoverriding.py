class Calculator:
    def add(self, a, b=None):
        if b is None:
            return a + a
        return a + b

calc = Calculator()
print(calc.add(5))     
print(calc.add(5, 10))

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

animal = Animal()
animal.speak()

dog = Dog()
dog.speak()
