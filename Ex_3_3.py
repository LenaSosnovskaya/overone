# Напишите классы Круг, Прямоугольник, Квадрат.
# Каждый класс должен содержать метод нахождения
# площади фигуры. Используйте: - Наследование - Абстрактный класс и методы
# - Округлите площадь круга до 2х чисел после запятой - Число π возьмите из модуля math
from abc import ABC, abstractmethod
import math

class Shapes(ABC):

    @abstractmethod
    def square(self):
        pass

class Circle(Shapes):

    def __init__(self, radius):
        self.radius = radius

    def square(self):
        return round(math.pi * self.radius**2, 2)

class Rectangle(Shapes):

    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width

    def square(self):
        return self.lenght * self.width

class Square_s(Shapes):

    def __init__(self, lenn):
        self.lenn = lenn

    def square(self):
        return self.lenn**2

c = Circle(5)
r = Rectangle(2,3)
s = Square_s(3)
print(c.square())
print(r.square())
print(s.square())

