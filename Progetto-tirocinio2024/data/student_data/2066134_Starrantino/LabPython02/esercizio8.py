a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

if a > 0 and b > 0 and c > 0:
    if a < b + c and b < a + c and c < a + b:
        if a == b and b == c:
            print('equilatero')
        elif (a == b and b != c) or (b == c and a != b):
            print('isoscele')
        else:
            print('scaleno')
else:
    print('input non valido')