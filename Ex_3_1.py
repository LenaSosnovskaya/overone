# Напишите функцию, которая будет принимать номер
# кредитной карты и показывать только последние 4 цифры.
# Остальные цифры должны заменяться звездочками

def card_hide(number_card):
    return '*' * (len(number_card)-4) + number_card[-4:]
print(card_hide('5456789515658562'))