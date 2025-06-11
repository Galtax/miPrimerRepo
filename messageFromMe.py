#Run with python Milo

for y in range(15, -15, -1):
    line = ""
    for x in range(-30, 30):
        formula = ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (x * 0.05) ** 2 * (y * 0.1) ** 3
        if formula <= 0:
            # alternar 0 y 1 para el efecto binario
            line += '1' if (x + y) % 2 == 0 else '0'
        else:
            line += ' '
    print(line)
