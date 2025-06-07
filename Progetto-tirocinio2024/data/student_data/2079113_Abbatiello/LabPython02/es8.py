a = input('inserisci lato :')
a = int(a)
b = input('inserisci lato :')
b = int(b)
c = input('inserisci lato :')
c = int(c)
if a > 0 and b > 0 and c > 0 :
    if a < b + c and b < c + a and c < b + a:
        if a != b and b !=c and a != c:
            print('triangolo scaleno')
        if a == b or a == c or b == c:
            print('triangolo isoscele')
        if a == b == c:
            print('triangolo equilatero')
    else:
     print('input non valido')
