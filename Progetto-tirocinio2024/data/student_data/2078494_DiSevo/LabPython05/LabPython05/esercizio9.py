b = int(input('Inserisci la base del rettangolo: '))
h = int(input("Inserisci l'altezza del rettangolo: "))

for i in range(h):
    for j in range(b):
        if (i==0) or (i==(h-1)):
            print('* ',end='')
        elif (j==0) or (j==(b-1)):
            print('* ',end='')
        else:
            print('  ',end='')
print()
