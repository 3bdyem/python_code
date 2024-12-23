class MyClass:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"MyClass with value: {self.value}"

    def __repr__(self):
        return f"MyClass({self.value})"

    def __add__(self, other):
        return MyClass(self.value + other.value)

    def __eq__(self, other):
        return self.value == other.value

    def __len__(self):
        return len(str(self.value))

    def __call__(self):
        return f"Called MyClass with value {self.value}"

obj1 = MyClass(10)
obj2 = MyClass(20)

print(str(obj1))  # __str__
print(repr(obj1))  # __repr__

obj3 = obj1 + obj2  # __add__
print(obj3)

print(obj1 == obj2)  # __eq__

print(len(obj1))  # __len__

print(obj1())  # __call__
