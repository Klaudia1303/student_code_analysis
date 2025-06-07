a = int(input('Inserire un numero:'))
b = int(input('Inserire un numero:'))
c = int(input('Inserire un numero:'))

if a != b != c and a>0 and b>0 and c>0:
    print('scaleno')
elif a == b == c and a>0 and b>0 and c>0:
    print('equilatero')
elif a == b or b == c or c == a and a>0 and b>0  and c>0:
    print('isoscele')
else:
    print('input non valido')
