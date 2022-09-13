def family_hide(lastname):
    return lastname[0].upper() + '*' * (len(lastname)-1)

print(family_hide('огурцова'))
