
#1
class Device:
    def __init__(self, name, model):
        self.name = name
        self.model = model

class CoffeeMachine(Device):
    def make_coffee(self):
        return "Кофе готов!"

class Blender(Device):
    def blend(self):
        return "Смесь готова!"

class MeatGrinder(Device):
    def grind(self):
        return "Мясо перемолото!"
    

#2
class Ship:
    def __init__(self, name, model):
        self.name = name
        self.model = model

class Frigate(Ship):
    def fire_cannons(self):
        return "Каноны стреляют!"

class Destroyer(Ship):
    def launch_missiles(self):
        return "Ракеты запущены!"

class Cruiser(Ship):
    def deploy_aircraft(self):
        return "Самолеты запущены!"
    
#1
import math

class Square:
    def __init__(self, side):
        self.side = side

class Circle:
    def __init__(self, radius):
        self.radius = radius

class CircleInSquare(Square, Circle):
    def __init__(self, side):
        Square.__init__(self, side)
        Circle.__init__(self, side / 2)


#2
class Wheels:
    def __init__(self, size):
        self.size = size

class Engine:
    def __init__(self, power):
        self.power = power

class Doors:
    def __init__(self, number):
        self.number = number

class Car(Wheels, Engine, Doors):
    def __init__(self, size, power, number):
        Wheels.__init__(self, size)
        Engine.__init__(self, power)
        Doors.__init__(self, number)


#3
class Shape:
    def show(self):
        pass

    def save(self):
        pass

    def load(self):
        pass

class Square(Shape):
    def __init__(self, x, y, side):
        self.x = x
        self.y = y
        self.side = side

class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

class Circle(Shape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

class Ellipse(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height