class Building:

    def __init__(self, doors, windows, floors):
        self.doors = doors
        self.windows = windows
        self.floors = floors

    def build(self):
        print("The building was built")

    def destroy(self):
        print("The building was destroyed")

class Beuty:

    def time(self, open_time, close_time):
       return f'Время работы салона: {open_time} - {close_time}'

    def manicur(self):
        pass

    def haircut(self):
        pass

    def salon_opening_hours(self, now_time):
        if now_time < self.open_time or now_time > self.close_time:
            return f'The shop is closed'
        else:
            return f'The shop is open'

class Building_with_Beuty(Building, Beuty):

    def __init__(self, doors, windows, floors, open_time, close_time):
        super().__init__(doors, windows, floors)
        self.open_time = open_time
        self.close_time = close_time

bwb = Building_with_Beuty(5,10,2,10,21)
print(bwb.salon_opening_hours(13))
print(bwb.salon_opening_hours(23))
print(bwb.time(bwb.open_time, bwb.close_time))





