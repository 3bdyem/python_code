class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive")

    def display_info(self):
        print(f"Name: {self.__name}, Age: {self.__age}")

person = Person("Ahmed", 30)
person.display_info()
print(person.get_name())
person.set_name("Mohamed")
person.set_age(35)
person.display_info()
