d = {1: 'ice-cream', 2: 'milk', 3: 'dog', 4: 'cat'}
for key in list(d.keys()):
    if key % 2 != 0:
        del d[key]
print(d)


