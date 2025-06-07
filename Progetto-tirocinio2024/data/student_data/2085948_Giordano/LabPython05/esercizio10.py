lato = int(input("Inserisci il lato del quadrato = "))

print("Hollow Square Star With Diagonals Pattern") 

for i in range(lato):
    for j in range(lato):
        if(i == 0 or i == lato - 1 or j == 0 or j == lato - 1
           or i == j or j == (lato - 1 - i)):
            print('* ', end = '')
        else:
            print('  ', end = '')
    print()