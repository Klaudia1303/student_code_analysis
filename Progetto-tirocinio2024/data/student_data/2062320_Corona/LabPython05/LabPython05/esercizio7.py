parola = input()
cont = 0


for let in parola:
    for c in range(0,len(parola)):
        if (let == parola[c]):
            cont = cont + 1
        else:
            cont = cont + 0
if (cont > len(parola)):
    print('true')
else:
    print('false')