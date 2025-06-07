n = int ( input ("inserire un numero dispari n: ") )
altezza = int(n/2)
for i in range (altezza, -1, -1):
    a = (n-(2*i))
    print (' '*i+'*'*a)

