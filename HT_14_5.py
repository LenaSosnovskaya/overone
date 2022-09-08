class Dog:

    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master
    def run(self):
        print(f'Dog run')
    def jump(self):
        print(f'Dog jump')
    def birthday(self):
        return self.age + 1
    def sleep(self):
        print(f'Dog sleep')
    def bark(self):
        print(f'Dog bark')

class Cat:

    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master
    def run(self):
        print(f'Cat run')
    def jump(self):
        print(f'Cat jump')
    def birthday(self):
        return self.age + 1
    def sleep(self):
        print(f'Cat sleep')
    def meow(self):
        print(f'Cat meow')

class Parrot:

    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master
    def run(self):
        print(f'Parrot run')
    def jump(self):
        print(f'Parrot jump')
    def birthday(self):
        return self.age + 1
    def sleep(self):
        print(f'Parrot sleep')
    def fly(self):
        print(f'Parrot fly')

