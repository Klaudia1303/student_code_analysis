a = int(input("inserire il valore d a: "))
b = int(input("inserire il valore di b: "))
c = int(input("inserire il valore di c: "))
if (a > 0 and b > 0 and c > 0):
    if ( a < (b+c) and b < (c+a) and c < (b+a)):
        if (a == b and b == c):
            print ("equilatero")
        elif (a != b and a != c and b != c):
            print ("scaleno")
        else:
            print ("isoscele")
    else:
        print ("input non valido")
else:
    print ("input non valido")
