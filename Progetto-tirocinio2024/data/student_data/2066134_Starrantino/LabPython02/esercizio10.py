age = int(input('age: '))
if (age > 0.0):
    out = 0
    deltaAge = age - 2
    if (deltaAge > 2):
        out += (4*deltaAge)
        print(out + 10.5*2)
    else:
        out += 10.5 * age
        print(out)
else:
    print('input non valido')