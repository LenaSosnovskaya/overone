class Pet:
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        return f'Pet run'

    def jump(self):
        return f'Pet jump'

    def birthday(self):
        self.age += 1

    def sleep(self):
        return f'Pet sleep'

class Dog(Pet):

    def bark(self):
        return f'Dog bark'

class Cat(Pet):

    def meow(self):
        return f'Cat meow'

class Parrot(Pet):

    def fly(self):
        return f'Parrot fly'

d = Dog('Archi', 5, 'Anna')
c = Cat('Musya', 10, 'Kate')
p = Parrot('Par', 3, 'Ivan')

print(d.bark(), c.meow(), p.fly(), sep=', ')
print(c.birthday())
print(c.__dict__)

