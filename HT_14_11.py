class Salon:

    min_price = 10

    def manicur(self):
        return f'Цена маникюра:{Salon.min_price * 1.2}'

    def haircut(self, lenght_hair):
        if lenght_hair < 30:
            return f'Цена стрижки:{Salon.min_price * 1.2}'
        elif 30 <= lenght_hair <= 50:
            return f'Цена стрижки:{Salon.min_price * 1.5}'
        else:
            return f'Цена стрижки:{Salon.min_price * 1.8}'

s = Salon()
print(s.manicur())
print(s.haircut(50))



