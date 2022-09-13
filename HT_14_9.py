from abc import ABC, abstractmethod

class NonNegativeValue:

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError(f'{self.name} cannot be negative')
        instance.__dict__[self.name] = value

class Pet:

    age = NonNegativeValue()
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    @abstractmethod
    def name_owner(self):
        pass

    def run(self):
        return f'Pet run'

    def jump(self):
        return f'Pet jump'

    def birthday(self):
        self.age += 1

    def sleep(self):
        return f'Pet sleep'

class Dog(Pet):

    def name_owner(self):
        return f'Name: {self.name}, owner: {self.master}'

    def bark(self):
        return f'Dog bark'

class Cat(Pet):

    def name_owner(self):
        return f'Name: {self.name}, owner: {self.master}'

    def meow(self):
        return f'Cat meow'

class Parrot(Pet):

    def name_owner(self):
        return f'Name: {self.name}, owner: {self.master}'

    def fly(self):
        return f'Parrot fly'

d = Dog('Archi', 5, 'Anna')
c = Cat('Musya', 10, 'Kate')
p = Parrot('Par', 3, 'Ivan')

print(d.bark(), c.meow(), p.fly(), sep=', ')
print(c.birthday())
print(c.__dict__)
print(p.name_owner())
print(d.__dict__)

