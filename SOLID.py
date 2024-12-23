# Single Responsibility Principle
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        return self.salary

class Report:
    def generate(self, employee):
        print(f"Employee Report for {employee.name}: Salary = {employee.get_salary()}")

employee = Employee("Ahmed", 5000)
report = Report()
report.generate(employee)

# Open/Closed Principle
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

shapes = [Rectangle(10, 5), Circle(7)]
for shape in shapes:
    print(shape.area())

# Liskov Substitution Principle
class Bird:
    def fly(self):
        pass

class Sparrow(Bird):
    def fly(self):
        print("Sparrow flies")

class Penguin(Bird):
    def fly(self):
        raise Exception("Penguins can't fly")

def make_bird_fly(bird):
    bird.fly()

sparrow = Sparrow()
penguin = Penguin()

make_bird_fly(sparrow)
make_bird_fly(penguin)

# Interface Segregation Principle
class Printer:
    def print_document(self, document):
        pass

class Scanner:
    def scan_document(self, document):
        pass

class MultiFunctionPrinter(Printer, Scanner):
    def print_document(self, document):
        print(f"Printing: {document}")

    def scan_document(self, document):
        print(f"Scanning: {document}")

printer = MultiFunctionPrinter()
printer.print_document("Doc1")
printer.scan_document("Doc2")

# Dependency Inversion Principle
class LightBulb:
    def turn_on(self):
        print("LightBulb is ON")

    def turn_off(self):
        print("LightBulb is OFF")

class Switch:
    def __init__(self, bulb):
        self.bulb = bulb

    def operate(self):
        self.bulb.turn_on()
        self.bulb.turn_off()

bulb = LightBulb()
switch = Switch(bulb)
switch.operate()
